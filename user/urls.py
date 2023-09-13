from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('my-page/<int:id>/profile-update/', views.profile_update_view, name='profile-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)