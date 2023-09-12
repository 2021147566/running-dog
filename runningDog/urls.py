from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.first_view, name='first_view'),
    path('second/', views.second_view, name='home'),
    path('signup/', views.sign_up_view, name='home'),
    path('signin/', views.sign_in_view, name='signin'),
    path('detail/', views.detail_view, name='signin'),
    path('mypage/', views.mypage_view, name='mypage'),
]
