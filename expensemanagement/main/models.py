from django.db import models
import datetime

# Create your models here.
class Friends(models.Model):
    username = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.datetime.now(),null=True)

    def __str__(self):
        return self.username
    
class SplitRecord(models.Model):
    paid = models.CharField(max_length=50)
    paymentList = models.JSONField()
    date = models.DateTimeField(default=datetime.datetime.now(),null=True)