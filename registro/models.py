from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#def get_image_filename(instance, filename):
#    title =  'titulo'
#    slug = slugify(title)
#    return "imagenesAvatares/%s-%s" % (slug, filename)  


#class Avatar(models.Model):
#    #vinvulo con el usuario
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
#    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

#    def __str__(self):
#        return f"Imagen de: {self.user.username}"

