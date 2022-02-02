from django.db import models

# Create your models here.

class Details(models.Model):
    amount = models.CharField(max_length=10)
    email = models.EmailField()

