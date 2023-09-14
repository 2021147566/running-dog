from django.shortcuts import render, redirect
from .models import UserModel
from .forms import CustomUserChangeForm
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def profile_update_view(request, id):
    my_profile = UserModel.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'my_profile.html', {'profile': my_profile})
    elif request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        form.save()
        try:
            my_profile.profile_pic = request.FILES['profile_pic']
        except:
            if my_profile.profile_pic:
                my_profile.profile_pic = my_profile.profile_pic
            else:
                my_profile.profile_pic = None
        my_profile.save()
        return redirect(f'/my-page/{ id }')


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'sign_up.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'sign_up.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'sign_up.html')
            else:
                UserModel.objects.create_user(username=username, password=password, email=email, bio=bio)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'sign_in.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')