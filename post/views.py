from django.shortcuts import render, redirect
from .models import PostModel


def home(request):
    return render(request, 'main.html')


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
        # TODO: 저장하고나서 해당 게시물 상세페이지로 이동하도록
        return redirect('/detail-page')

def detail_page_view(request):
    return render(request, 'detail_page.html')


def my_page_view(request):
    return render(request, 'my_page.html')