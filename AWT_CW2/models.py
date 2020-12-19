from django.db import models

class ClassModel(models.Model):
    country = models.CharField(max_length=20)
    recovered= models.CharField(max_length=20)
    positive = models.CharField(max_length=20)
    death = models.CharField(max_length=20)

