from django.db import models


# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

movies_choices=(('A','Action'),('H','horror'),('T','Thriller'))
class Film(models.Model):
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    tags=models.CharField(choices=movies_choices,max_length=20)
    R_rating=models.CharField(max_length=20)
    Description=models.TextField()
    image_url=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
