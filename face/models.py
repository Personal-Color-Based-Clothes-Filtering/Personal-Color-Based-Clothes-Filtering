from django.db import models

# Create your models here.
# 파일 업로드
class FaceImage(models.Model) : 
    faceId = models.AutoField(primary_key=True)
    faceImg = models.ImageField(upload_to='images/') 
