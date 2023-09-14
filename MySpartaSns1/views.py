from django.http import HttpResponse
from django.shortcuts import render

def base_response(request):
    return HttpResponse("페이지를 불러옵니다.")

def first_view(request):
    return render(request,'base.html')