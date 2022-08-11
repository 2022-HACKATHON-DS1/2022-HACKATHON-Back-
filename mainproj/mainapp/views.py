from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date')[:5]
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def mypage(request):
    # /?year=2022
    year = request.GET.get('year', None)
    print(year)

    if year is None:
        posts = Post.objects.all().order_by('-date')
    else:
        posts = Post.objects.filter(date__year=year)

    return render(request, 'mypage.html', {'posts':posts})