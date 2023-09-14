from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(label='이름', max_length=100)
    email = forms.EmailField(label='이메일')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

class SignInForm(forms.Form):
    login_email = forms.EmailField(label='이메일')
    login_password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
