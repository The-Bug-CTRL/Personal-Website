from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog_home, name='blog_home'),  # Use 'blog_home' instead of 'blog'

    path('',  # Use class-based view for the root URL
         ListView.as_view(
             queryset=Post.objects.all().order_by("-date")[:25],
             template_name="blog.html"
         ),
    ),
    path('<int:pk>/',
         DetailView.as_view(
             model=Post,
             template_name="post.html"
         ),
    ),
]
