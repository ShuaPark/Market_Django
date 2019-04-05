from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Photo(models.Model):
    author  = models.ForeignKey(User, 
        on_delete = models.CASCADE, 
        related_name = 'user_photos')

    # app폴더/photos/%y/%m/%d/ 에 파일을 저장 : 
    # 아래의 경우는 App별로 다른 폴더가 생성됩니다
    photo   = models.ImageField(upload_to = 'photo/%y/%m/%d', 
        default = 'photos/on_image.png')
    text    = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse("photo:photo_detail", arg=[str(self.id)])
    