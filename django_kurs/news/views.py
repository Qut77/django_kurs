from django.shortcuts import render, redirect
from .models import articles
from .forms import articles_form
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = articles.objects.all()
    data = {
        'title': 'Новости на сайте',
        'h1':'Новости',
        'text':'сенсация',
        'news':news
    }
    return render(request, 'news/news_home.html', data)

class news_detail(DetailView):
    model=articles
    template_name='news/news_detail.html'
    context_object_name = 'article'

class news_update(UpdateView):
    model=articles
    template_name='news/create.html'
    form_class = articles_form

class news_delete(DeleteView):
    model=articles
    template_name='news/news_delete.html'
    success_url ='/news/'

def create(request):
    error = ''
    if request.method == 'POST':
        form = articles_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = articles_form()
    data ={
        'title':'Создание новости',
        'h1':'Создание новости',
        'text': 'Создайте свою новость',
        'form':form,
        'error': error
    }
    return render(request, 'news/create.html', data)

