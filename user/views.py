# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, SignInForm
from .models import UserModel
from django.http import HttpResponse

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password != password2:
                return render(request, 'base.html', {'form': form, 'error_message': '비밀번호가 일치하지 않습니다.'})

            if UserModel.objects.filter(email=email).exists():
                return render(request, 'base.html', {'form': form, 'error_message': '이미 등록된 이메일 주소입니다.'})

            hashed_password = make_password(password)
            new_user = UserModel(name=name, password=hashed_password, email=email)
            new_user.save()

            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return HttpResponse('회원가입 하셨습니다!')

    else:
        form = SignUpForm()

    return render(request, 'base.html', {'form': form})

def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['login_email']
            password = form.cleaned_data['login_password']

            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('success_url')  # 로그인 성공 후 url
            else:
                return render(request, 'base.html', {'form': form, 'error_message': '로그인 실패: 이메일 또는 비밀번호가 올바르지 않습니다.'})
    else:
        form = SignInForm()

    return render(request, 'base.html', {'form': form})
