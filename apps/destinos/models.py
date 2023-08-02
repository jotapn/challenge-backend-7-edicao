from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
import os

class Destino(models.Model):
    '''Modelo dos Destinos'''
    def upload_path_1(instance, filename):
        '''Criando caminho para as'''
        type_file = filename.split(".")[-1]
        filename = instance.nome.replace(" ", "_") + "1." + type_file
        return f'destinos/{filename}'
    
    def upload_path_2(instance, filename):
        '''Criando caminho para as'''
        type_file = filename.split(".")[-1]
        filename = instance.nome.replace(" ", "_") + "2." + type_file
        return f'destinos/{filename}'

    foto_1 = models.ImageField(
        verbose_name='Foto 1',
        null = True,
        blank=True,
        upload_to= upload_path_1)
    
    foto_2 = models.ImageField(
        verbose_name='Foto 2',
        null = True,
        blank=True,
        upload_to= upload_path_2)
    
    nome = models.CharField(
        verbose_name='Nome',
        max_length=40,
        null = False,
        blank = False)
    
    meta = models.CharField(
        max_length=160,
        default= None,
        null=False)

    texto_descritivo = models.TextField(
        verbose_name='Texto Descritivo',
        default= None,
        null=True,
        blank= True)

    preco = models.IntegerField(
        verbose_name='Preço',
        null = False,
        blank = False)

    def __str__(self) -> str:
        return self.nome
    