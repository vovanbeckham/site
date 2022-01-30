from django.shortcuts import render, redirect

from .forms import *
from .models import *

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить тему", 'url_name': 'add_page'},
        ]


def add_bd(t_id: int):
    pass


def index(request):
    posts = Threads.objects.all().order_by('-time_update')
    #mess = Message.objects.all()
    context = {
        'posts': posts,
        #: mess,
        'menu': menu,

    }
    return render(request, 'first/index.html', context=context)


def about(request):
    return render(request, 'first/about.html', {'menu': menu})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            k = form.save(commit=False)

            k.save()
            return redirect('post', k.pk)
    else:
        form = AddPostForm()
    context = {'form': form,
               'menu': menu,
               'title': 'Добавление темы'}
    return render(request, 'first/addpage.html', context=context)


def show_post(request, post_id):
    mess = Message.objects.filter(parent_id=post_id)
    posts = Threads.objects.all
    if request.method == 'POST':
        form = AddThreadForm(request.POST)

        if form.is_valid():
            m = form.save(commit=False)
            m.parent_id = post_id
            if not m.syga:
                p = Threads.objects.get(pk=post_id)
                p.count = p.count + 1
                p.save()
            m.save()

            return redirect('post', post_id)
    else:
        form = AddThreadForm(initial={'parent': post_id})
    context = {
        'form': form,
        'post_id': post_id,
        'posts': posts,
        'mess': mess,
        'menu': menu,
        'title': 'Главная страница'

    }

    return render(request, 'first/thread.html', context=context)


