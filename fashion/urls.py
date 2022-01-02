from django.urls import path
from . import views
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name = 'main'),
    path('image_upload/', views.face_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    path('shopping/', views.musinsa_fashion, name='musinsa'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)