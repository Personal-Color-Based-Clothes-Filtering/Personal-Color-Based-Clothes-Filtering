from django.urls import path
from . import views
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'fashion'

urlpatterns = [
    path('', views.all_list, name='all_list'), 
    path('list/spring/', views.spring_list, name='spring_list'),  
    path('list/summer/', views.summer_list, name='summer_list'),  
    path('list/autumn/', views.autumn_list, name='autumn_list'),  
    path('list/winter/', views.winter_list, name='winter_list'),  
]