from django.urls import path
from . import views
from .views import * 

app_name = 'face'

urlpatterns = [
    path('', views.face_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
]