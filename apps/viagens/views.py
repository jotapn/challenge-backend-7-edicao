import random
from rest_framework import viewsets
from .models import Depoimento
from .serializer import DepoimentoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated

class DepoimentoViewSet(viewsets.ModelViewSet):
    ''' Exibindo todos os depoimentos '''
    queryset = Depoimento.objects.all()   
    serializer_class = DepoimentoSerializer

class DepoimentoHomeViewSet(viewsets.ModelViewSet):
    '''Listando 3 depoimentos aleatórios'''
    serializer_class = DepoimentoSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset

    @method_decorator(cache_page(10))
    def dispatch(self, *args, **kwargs):
        return super(DepoimentoHomeViewSet, self).dispatch(*args, **kwargs)

    
    
