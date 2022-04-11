from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200) 
    content= models.TextField()

    def __str__(self):
        return self.title 

# __str__: 해당 출력하는 함수에서 return 값을 title로