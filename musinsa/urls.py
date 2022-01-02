"""musinsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include

# 이미지 업로드 관련
from django.conf.urls.static import static
from django.conf import settings
#from .views import *
from fashion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fashion.urls')),

    path('image_upload/', views.face_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    path('shopping/', views.musinsa_fashion, name='musinsa'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
