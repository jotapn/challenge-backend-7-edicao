from rest_framework import viewsets, filters, status
from .models import Destino
from .serializer import DestinoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class DestinosViewSet(viewsets.ModelViewSet):
    ''' Exibindo todos os destinos '''  
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
    ordering_fields = ['nome', 'preco']
    filterset_fields = ['nome']
    search_fields = ['nome']

    def list(self, request):
            queryset = self.filter_queryset(self.get_queryset())
            if not queryset.exists():
                return Response({"mensagem": "Nenhum destino encontrado."}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)        