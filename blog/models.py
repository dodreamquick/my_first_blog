from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
    #category를 대표하는 문자열

class Post(models.Model):
    
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL, #장고의 user model 확장
        on_delete=models.CASCADE # 필수
        
    )
    
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, default=None, null=True, blank=True) #category delete하면 post가 삭제되는 게 아니라 post의 category만 Null이 되게끔. blank=True는 blank(null)로 지정해도 낼 수 있다(포스트를 저장할 수 있다)
    
    title = models.CharField(max_length=200)
    
    text = models.TextField()
    
    created_date=models.DateTimeField(
        default=timezone.now
    )
    
    published_date = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
    )
    
    def publish(self) :
        self.published_date=timezone.now()
        self.save()
        
    def __str__(self):
        return self.title