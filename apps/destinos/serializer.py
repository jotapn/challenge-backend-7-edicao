from rest_framework import serializers
from .models import Destino

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

    
    search_fields = ['nome']