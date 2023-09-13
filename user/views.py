from django.shortcuts import render, redirect
from .models import UserModel
from .forms import CustomUserChangeForm


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
