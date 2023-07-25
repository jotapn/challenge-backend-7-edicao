from rest_framework.test import APITestCase
from apps.destinos.models import Destino
from django.urls import reverse
from rest_framework import status

class DestinoTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Destinos-list')
        self.destino = Destino.objects.create(
            foto= None,
            nome= 'Rio de Janeiro',
            preco= 1000.0,
        )
        
        self.objeto_url = reverse('Destinos-list') + f'{self.destino.id}/'
    
    def test_requisicao_get_para_listar_destinos(self):
        '''Teste para verificar a requisição GET para listar os destinos'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_requisicao_post_para_criar_destino(self):
        '''Teste para verificar a requisição POST para criar um destino'''

        data = {
            'foto': '',
            'nome': 'Nome teste 3',
            'preco': 120.0,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_destino(self):
        """Teste para atualizar destino"""
        data = {
            'id': self.destino.id,
            'foto':'',
            'nome':'São Paulo',
            'preco':100.0,
        }
        response = self.client.put(path=self.objeto_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_destino(self):
        """Teste para deletar destino"""
        response = self.client.delete(self.objeto_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)