from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveAPIView)
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["publish_date", "create_date"]
    ordering = ["-create_date"]

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'
