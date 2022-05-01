from django.db import models

# Create your models here.


class user_admin(models.Model):
    username = models.CharField(max_length=40, default="")
    email = models.CharField(max_length=35, unique=True, primary_key=True)
    password = models.CharField(max_length=20)
    # gello
