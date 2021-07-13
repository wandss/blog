from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
