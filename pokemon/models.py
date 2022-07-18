from pyexpat import model
from django.db import models

# Create your models here.
class Pokemon (models.Model):

    PokemonType={
        ("WATER", "WA"),
        ("GRASS", "GR"),
        ("GHOST" , "GH"),
        ("STEEL" ,"ST"),
        ("FAIRY" ,"FA"),
    }
    name = models.CharField(max_length=30)
    type = models.CharField(choices=PokemonType,max_length=250,)
    hp = models.PositiveBigIntegerField()
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30,default="")
    name_ar = models.CharField(max_length=30,default="")
    name_jp = models.CharField(max_length=30,default="")
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    



