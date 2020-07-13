from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blogs(request):
    entries = Blog.objects.all()[:5]
    context = {
        'entries': entries,
        'number_posts': Blog.objects.count()
    }
    return render(request, 'blog/all_blogs.html', context)


def detail(request, pk):
    article = get_object_or_404(Blog, id=pk)
    context = {
        'title': article.title,
        'description': article.description,
        'date': article.date
    }
    return render(request, 'blog/detail.html', context)
