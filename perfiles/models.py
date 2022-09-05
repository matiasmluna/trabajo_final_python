from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from django.db import models

class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_image/',black=True)

class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"