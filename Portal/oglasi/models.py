from django.db import models
from django.contrib.auth.models import User

class Oglas(models.Model):
    naslov = models.CharField(max_length = 50)
    tekst = models.TextField(blank = True)
    datum = models.DateTimeField(auto_now_add = True)
    opcije = (
        ('1', 'Korisnici'),
        ('2', 'Volonteri'),
    )
    vidljivost = models.CharField(max_length = 1, choices = opcije, default = '1')
    za_brisanje = models.BooleanField(default = False)
    arhiviran = models.BooleanField(default = False)
    autor = models.OneToOneField(User, on_delete = models.CASCADE)
