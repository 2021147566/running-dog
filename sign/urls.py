from django.urls import path
from sign import views

urlpatterns = [
    path('sign/', views.index, name='index'),
]
