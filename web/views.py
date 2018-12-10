from django.core.paginator import Paginator
from django.shortcuts import render

from backweb.models import Article, AType


def index(request):
    if request.method == 'GET':
        data = Article.objects.all()
        type = AType.objects.all()
        return render(request, 'web/index.html',{'type': type, 'data': data})
    if request.method == 'POST':
        img = Article.objects.all()
        type = AType.objects.all()
        msg = request.POST.get('keyboard')
        page = int(request.GET.get('page', 1))
        article = Article.objects.filter(title__contains=msg, is_show=1)
        paginator = Paginator(article, 20)
        pages = paginator.page(page)
        alert = ''
        if not article:
            alert = '搜索为空'
        return render(request, 'web/index.html', {'pages': pages, 'alert': alert, 'type': type, 'img':img})


def share(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 20)
        pages = paginator.page(page)
        return render(request, 'web/share.html', {'pages': pages})


def info(request):
    if request.method == 'GET':
        types = AType.objects.all()
        page = int(request.GET.get('page', 1))
        articles = Article.objects.filter(is_show=1)
        paginator = Paginator(articles, 1)
        pages = paginator.page(page)
        return render(request, 'web/info.html', {'pages': pages, 'types': types, 'articles': articles})
    if request.method == 'POST':
        msg = request.POST.get('keyboard')
        types = AType.objects.all()
        article = Article.objects.filter(is_show=1, title__contains=msg)
        articles = Article.objects.filter(is_show=1)
        page = int(request.GET.get('page', 1))
        paginator = Paginator(article, 1)
        pages = paginator.page(page)
        alert = ''
        if not article:
            alert = '未搜索到文章'
        return render(request, 'web/info.html', {'pages': pages, 'types': types, 'articles': articles, 'alert': alert})




