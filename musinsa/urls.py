from django.contrib import admin
from django.urls import path, include

# 이미지 업로드 관련
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('main.urls')),
    path('admin/', admin.site.urls),
    path('shopping/', include('fashion.urls')),
    path('face/', include('face.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
