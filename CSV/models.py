from django.db import models

class Users(models.Model):
    Usuario = models.CharField(max_length=255,unique=True)
    Password = models.CharField(max_length=50)

class Contactar(models.Model):
    Usuario = models.CharField(max_length=255,unique=True)
    Mensaje = models.CharField(max_length=1000)

# Create your models here.
