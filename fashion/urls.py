from django.urls import path
from . import views
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'fashion'

urlpatterns = [
    path('list/', views.all_list, name='all_list'), 
    # path('', views.musinsa_fashion, name='musinsa'),  
    path('', views.tmp_musinsa_view, name='musinsa'),  
]