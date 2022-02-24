from django.db import models

# 이미지 업로드
class FaceImage(models.Model) : 
    faceId = models.AutoField(primary_key=True)
    faceImg = models.ImageField(upload_to='images/') 
