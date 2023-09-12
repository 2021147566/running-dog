from django.shortcuts import render


def first_view(request):
    return render(request, 'post_page.html')


def second_view(request):
    return render(request, 'my_test2.html')


def sign_up_view(request):
    return render(request, 'sign_up.html')


def sign_in_view(request):
    return render(request, 'sign_in.html')


def detail_view(request):
    return render(request, 'detail_page.html')


def mypage_view(request):
    return render(request, 'my_page.html')