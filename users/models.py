from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile = models.ImageField(upload_to="profile_images/",default="default/profile.png")
    cover = models.ImageField(upload_to="cover_images/",default="default/fon.png")
    followers = models.ManyToManyField("self",blank=True)
    following = models.ManyToManyField("self",blank=True)
    verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=200,null=True,blank=True)
    birth_of_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.username