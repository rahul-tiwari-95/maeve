from django.apps import apps
from django.db.models import JSONField
from django.db import models
from django.utils import timezone
import datetime


# Creating models for Maeve.


class UserAuth(models.Model):
    name = models.CharField(max_length=255)
    metauserID = models.IntegerField(default=1)
    #Execute metauserauth code to verify credentials of the user  
    locationCoordinates = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "MetauserID: %s" % (self.name)



class UserInput(models.Model):
    userAuthID = models.ForeignKey(UserAuth, on_delete=models.PROTECT)
    text = models.CharField(max_length=500)
    sentimentAnalysis = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User Input: %s" % (self.text)


class MaeveResponse(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)
