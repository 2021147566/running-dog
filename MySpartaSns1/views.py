from django.http import HttpResponse
from django.shortcuts import render

def base_response(request):
    return HttpResponse("뭘봐 시발년아")

def first_view(request):
    return render(request,'my_test.html')