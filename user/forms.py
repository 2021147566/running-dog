from django.contrib.auth.forms import UserChangeForm
from .models import UserModel


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'bio']