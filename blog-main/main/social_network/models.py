from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True, null=True)
    page = models.OneToOneField('Profile', on_delete=models.CASCADE, null=True)
    commentaries = models.ForeignKey('Message', on_delete=models.CASCADE, null=True, blank=True)


class Profile(models.Model):
    date_birth = models.DateField(blank=True, default=None, null=True)
    status = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)


class Message(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    page = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='comments_image', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    destination = models.CharField(max_length=300, null=True, blank=True)
