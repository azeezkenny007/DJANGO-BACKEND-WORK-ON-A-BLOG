from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return self.name+' '+self.email