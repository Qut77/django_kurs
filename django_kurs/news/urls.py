from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.news_detail.as_view(), name='news_detail'),
    path('<int:pk>/update', views.news_update.as_view(), name='news_update'),
    path('<int:pk>/delete', views.news_delete.as_view(), name='news_delete')
]
