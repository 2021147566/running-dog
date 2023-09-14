from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('my-page/<int:id>/profile-update/', views.profile_update_view, name='profile-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)