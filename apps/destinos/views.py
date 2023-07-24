from rest_framework import viewsets
from .models import Destino
from .serializer import DestinoSerializer

class DestinosViewSet(viewsets.ModelViewSet):
    ''' Exibindo todos os destinos '''
    queryset = Destino.objects.all()   
    serializer_class = DestinoSerializer
