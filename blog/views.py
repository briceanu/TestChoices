from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics



class CreateBlogs(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ListBlogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

