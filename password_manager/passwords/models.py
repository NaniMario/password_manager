from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserPassword(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    app = models.CharField(max_length=30,)
    password = models.CharField(max_length=30,)
    

    def __str__(self):
        return self.app
