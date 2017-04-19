from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    playerRights = models.IntegerField(default=0, blank=True)
    blackMarks = models.IntegerField(default=0, blank=True)
    timePlayed = models.BigIntegerField(default=0, blank=True)
    ipAddress = models.GenericIPAddressField(default=0)
    def __str__(self):
        return self.user.get_username()