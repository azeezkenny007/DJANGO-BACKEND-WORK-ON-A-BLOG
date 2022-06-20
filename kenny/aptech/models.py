from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=250)
    body=models.TextField()
    references=models.CharField(max_length=250,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)


