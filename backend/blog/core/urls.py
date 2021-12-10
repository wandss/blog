from django.urls import path
from .views import PostListAPIView, PostRetrieveAPIView, PublishedListAPIVIew

urlpatterns = [
        path('posts/', PostListAPIView.as_view(), name='get_create_posts'),
        path('posts/<post_id>', PostRetrieveAPIView.as_view(), name='get_post'),
        path('posts/published/', PublishedListAPIVIew.as_view(),
              name='get_published'),
    ]

