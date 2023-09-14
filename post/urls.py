from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('post-page/', views.post_page_view, name='post-page'),
    path('detail-page/<int:id>', views.detail_page_view, name='detail-page'),
    path('my-page/<int:id>', views.my_page_view, name='my-page'),
    path('my-page/<int:id>/my-feed/', views.my_feed_view, name='my-feed'),
    path('other-page/<int:id>', views.other_page_view, name='my-page'),
    path('detail-page/<int:id>/delete', views.delete_page_view, name='delete-page'),
    path('detail-page/<int:id>/update', views.update_page_view, name='update-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)