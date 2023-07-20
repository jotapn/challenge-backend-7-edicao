import random
from rest_framework import viewsets, generics
from .models import Depoimento
from .serializer import DepoimentoSerializer


class DepoimentoViewSet(viewsets.ModelViewSet):
    ''' Exibindo todos os depoimentos '''
    queryset = Depoimento.objects.all()   
    serializer_class = DepoimentoSerializer

class DepoimentoHomeViewSet(viewsets.ModelViewSet):
    '''Listando 3 depoimentos aleatórios'''
    serializer_class = DepoimentoSerializer
    allowed_methods = ['GET']
    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset