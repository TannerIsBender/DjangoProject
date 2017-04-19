from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    playerName = models.CharField(max_length=20)
    playerRights = models.IntegerField(default=0)
    def __str__(self):
        return self.playerName

class Users(models.Model):
    playerName = models.CharField(max_length=20)
    playerPass = models.CharField(max_length=25)
    playerRights = models.IntegerField(default=0)
    blackMarks = models.IntegerField(default=0)
    timePlayed = models.BigIntegerField(default=0)
    ipAddress = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.playerName