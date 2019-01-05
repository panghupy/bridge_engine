from news.models import News

from django.shortcuts import render, redirect, reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 返回所有新闻
def index(request):
    all_news = News.objects.all()

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(all_news, 20)

    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)

    # 把当前的页码数转换成整数类型
    currentPage = int(page)

    try:
        all_news = paginator.page(currentPage)  # 获取当前页码的记录
    except PageNotAnInteger:
        all_news = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    # 显示前5页
    page_back = currentPage - 5
    # 显示后5页
    page_go = currentPage + 5
    ctx = {
        'all_news': all_news
    }

    return render(request, 'index.html', locals())


def search(request):
    keyword = request.POST.get('keyword', '建筑')
    search_news = News.objects.filter(keyword=keyword)

    # 生成paginator对象,定义每页显示10条记录
    paginator = Paginator(search_news, 20)

    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)

    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    # 显示前5页
    page_back = currentPage - 5
    # 显示后5页
    page_go = currentPage + 5
    try:
        search_news = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        search_news = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        search_news = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    ctx = {
        'search_news': search_news
    }

    return render(request, 'search.html', locals())
