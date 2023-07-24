from django.db import models

class Depoimento(models.Model):
    def upload_path(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome.replace(" ", "_") + "." + type_file
        return f'depoimentos/{filename}'

    foto = models.ImageField(upload_to= upload_path, blank=True, null= True)
    nome = models.CharField(max_length=50)
    depoimento = models.TextField(max_length=200)

    def __str__(self):
        return self.depoimento