from django.shortcuts import render, redirect
from .forms import RegistrationForm
def index(request):
    return render(request, 'sign/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'sign/index.html', {'form': form})