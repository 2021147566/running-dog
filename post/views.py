from django.shortcuts import render, redirect
from .models import PostModel, UserModel


def home(request):
    if request.method == 'GET':
        all_post = PostModel.objects.all().order_by('-updated_at')
        return render(request, 'main.html', {'post': all_post})


def post_page_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'post_page.html')
        else:
            # TODO: 로그인 안 했을 경우 로그인 페이지로 이동
            return redirect('/')
    elif request.method == 'POST':
        # 새 게시물 생성
        user = request.user
        mypost = PostModel()
        mypost.author = user
        mypost.place_name = request.POST.get('my-place', '')
        mypost.contents = request.POST.get('my-content', '')
        # 이미지 공백 시 에러 발생 방지
        try:
            mypost.image = request.FILES['image']
        except:
            mypost.image = None
        mypost.save()
        return redirect(f'/detail-page/{ mypost.id }')


def detail_page_view(request, id):
    # return render(request, 'detail_page.html')
    if request.method == 'GET':
        detail_page = PostModel.objects.get(id=id)
        return render(request, 'detail_page.html', {'detail': detail_page})


def my_page_view(request, id):
    if request.method == 'GET':
        user = UserModel.objects.get(id=id)
        return render(request, 'my_page.html', {'user': user})


def my_feed_view(request, id):
    if request.method == 'GET':
        my_feed = PostModel.objects.filter(author_id=id).order_by('-updated_at')
        return render(request, 'my_feed.html', {'feed': my_feed})


def other_page_view(request, id):
    if request.method == 'GET':
        other = UserModel.objects.get(id=id)
        return render(request, 'other_page.html', {'other': other})