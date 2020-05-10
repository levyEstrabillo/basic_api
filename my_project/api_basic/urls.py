from django.urls import path
from .views import article_list, article_detail

app_name='articles'

urlpatterns = [
    path('', article_list, name='list'),
    path('<int:id>', article_detail, name='detail'),
]