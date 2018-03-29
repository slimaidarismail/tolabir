from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Test(models.Model):
    title = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="img/tafaha")
    genre_choices = (('f', 'female'),('m', 'male'))
    genre = models.CharField(max_length=100,choices=genre_choices)
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    height = models.IntegerField(default=400)
    width = models.IntegerField(default=800)

    def __str__(self):
        return self.title



class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, upload_to="img/tafaha")

    def __str__(self):
        return "Choice for : {}".format(self.test)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField(upload_to="img/users")