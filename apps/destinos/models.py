from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
import os

class Destino(models.Model):
    def upload_path(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome.replace(" ", "_") + "." + type_file
        return f'destinos/{filename}'

    foto = models.ImageField(
        verbose_name='Imagem',
        null = True, blank=True,
        upload_to= upload_path)
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=30,null = False,
        blank = False)
    
    preco = models.FloatField(
        verbose_name='Preço',
        max_length=10,
        null = False,
        blank = False)

    def __str__(self) -> str:
        return self.nome
    
@receiver(pre_delete, sender=Destino)
def handler_pre_delete(sender, instance, **kwargs):
    os.remove(instance.foto.path)