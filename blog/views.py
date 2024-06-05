from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import (
    Post,
)

def http_405():
    return HttpResponse(
        '<p>Method Not Allowed</p>',
        content_type='text/html',
        status=405,
    )

def list_posts(request):
    if request.method != "GET":
        return http_405()        
    posts = Post.objects.order_by('-modified')
    return render(
        request=request,
        template_name='blog/list_posts.html',
        context={
            'posts': posts,
        },
    )

def post_detail(request, slug):
    if request.method != "GET":
        return http_405()        
    post = get_object_or_404(Post, slug=slug)
    return render(
        request=request,
        template_name='blog/post_detail.html',
        context={
            'post': post,
        },
    )
