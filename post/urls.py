from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-page/', views.post_page_view, name='post-page'),
    path('detail-page/', views.detail_page_view, name='detail-page'),
    path('my-page/', views.my_page_view, name='my-page'),
]