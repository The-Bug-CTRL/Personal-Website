
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def blog_home(request):
    return render(request, 'blog/blog.html')