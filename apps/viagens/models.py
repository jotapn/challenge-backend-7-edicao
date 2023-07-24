from django.db import models

class Depoimento(models.Model):
    foto = models.ImageField(blank=True, null= True)
    depoimento = models.TextField(max_length=200)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.depoimento