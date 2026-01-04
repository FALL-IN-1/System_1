from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__ (self):
        return f"{self.name.username}'s profile"
