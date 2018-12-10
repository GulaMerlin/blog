from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.Artform import Artform, Editform
from backweb.models import User, Article


def index(request):
    if request.method == 'GET':

        return render(request, 'backweb/index.html')


def login(request):
    if request.method == 'GET':

        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        ob_user = User.objects
        if ob_user.filter(username=username):
            if ob_user.filter(username=username, password=password):
                request.session['user_id'] = ob_user.filter(username=username, password=password).first().id
                return HttpResponseRedirect(reverse('backweb:index'))
            else:
                err_data = '密码错误'
                return render(request, 'backweb/login.html', {'err_data': err_data})
        err_data = '账号错误'
        return render(request, 'backweb/login.html', {'err_data': err_data})
        # return render(request, 'backweb/login.html', {'err_data': err_data})


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')
    username = request.POST.get('username')
    password = request.POST.get('userpwd')
    repassword = request.POST.get('reuserpwd')
    ob_user = User.objects
    if ob_user.filter(username=username):
        err_data = '该账号已注册，请换一个账号'
        return render(request, 'backweb/register.html', {'err_data': err_data})
    if password != repassword:
        err_data = '两次密码不同！请重新输入！'
        return render(request, 'backweb/register.html', {'err_data': err_data})
    else:
        ob_user.create(username=username, password=password)
        return HttpResponseRedirect('/backweb/login/')


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.filter(is_show=1)
        paginator = Paginator(articles, 3)
        pages = paginator.page(page)
        return render(request, 'backweb/article.html', {'pages': pages})


def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')
    if request.method == 'POST':
        form = Artform(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            category = int(form.cleaned_data['category'])
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, types_id=category, icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            return render(request, 'backweb/add_article.html', {'form': form})


def edit_article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add_article.html', {'article':article})
    if request.method == 'POST':
        form = Editform(request.POST, request.FILES)
        if form.is_valid():
            # 验证成功
            title = form.cleaned_data['title']
            desc = form.cleaned_data.get('desc')
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            article.icon = icon
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            # 验证失败
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/article.html', {'form': form, 'article': article})

def del_article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        article.is_show=0
        article.save()
        return HttpResponseRedirect(reverse('backweb:article'))