from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.


def showblog(request):
    blog_post = BlogPost.objects
    return render(request, 'blog/blog.html', {'blogpost': blog_post})


def specific_post(request, post_id):
    that_post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': that_post})