from .views import *
from django.urls import path
urlpatterns = [
    path('', news_list, name='news_list_url'),
   	path('news/add/', NewsAdd.as_view(), name='news_add_url'),
    path('news/<str:id>/', news_detail, name='news_detail_url'),

]