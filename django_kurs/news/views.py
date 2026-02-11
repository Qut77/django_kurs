from django.shortcuts import render

def news_home(request):
    data ={
        'title': 'Новости на сайте',
        'h1':'Новости',
        'text':'сенсация'
    }
    return render(request, 'news/news_home.html', data)