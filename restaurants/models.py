from django.db import models
import datetime

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
