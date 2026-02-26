from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_en, name='index'),
    path('zh-cn/', views.index_zh, name='index-zh'),
]
