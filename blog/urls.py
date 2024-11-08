from django.urls import  path
from . import views

urlpatterns=[
    path('create',views.CreateBlogs.as_view(), name='create_blog'),
    path('list',views.ListBlogs.as_view(),name='list_blogs')
    ]