from django.db import models

class Destino(models.Model):
    def upload_path(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome.replace(" ", "_") + "." + type_file
        return f'destinos/{filename}'

    foto = models.ImageField(verbose_name='Imagem', null = True, blank=True, upload_to= upload_path)
    nome = models.CharField(verbose_name='Nome', max_length=30,null = False, blank = False)
    preco = models.CharField(verbose_name='Preço', max_length=10,null = False, blank = False)

    def __str__(self) -> str:
        return self.nome