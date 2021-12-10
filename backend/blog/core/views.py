from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateAPIView)
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["publish_date", "create_date"]
    ordering = ["create_date"]

class PublishedListAPIVIew(ListAPIView):
    queryset = Post.objects.all().exclude(publish_date=None)
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["publish_date", "create_date"]
    ordering = ["create_date"]


class PostRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'

#TODO: Close the API and open specific endpoints to be available without
#authentication
