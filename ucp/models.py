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
        
class Ban(models.Model):
    bannedPlayer = models.CharField(max_length=20)
    bannedBy = models.CharField(max_length=20)
    reason = models.TextField(blank=True)
    canAppeal = models.BooleanField(default=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    
class Report(models.Model):
    target = models.CharField(max_length=20)
    reporter = models.CharField(max_length=20)
    reason = models.TextField(blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.target
    
class Appeal(models.Model):
    banID = models.IntegerField(default=0)
    appealField = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)