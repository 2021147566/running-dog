from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.sign_up_view, name='sign-up'),
    path('sign/', views.sign_in_view, name='sign-in'),
]