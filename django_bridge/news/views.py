from news.models import News

from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse


# 返回所有新闻
def index(request):
    all_news = News.objects.all()
    ctx = {
        'all_news': all_news
    }

    return render(request, 'index.html', ctx)


def search(request):
    keyword = request.POST.get('keyword', '建筑')
    search_news = News.objects.filter(keyword=keyword)
    ctx = {
        'search_news': search_news
    }

    return render(request, 'search.html', ctx)
