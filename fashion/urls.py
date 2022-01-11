from django.urls import path
from . import views
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'fashion'

urlpatterns = [
    path('', views.musinsa_fashion, name='musinsa'),  
]