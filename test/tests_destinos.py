from rest_framework.test import APITestCase
from apps.destinos.models import Destino
from django.urls import reverse
from rest_framework import status

class DestinosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Destinos-list')
        self.destino = Destino.objects.create(
            foto_1= 'teste',
            foto_2= 'testee',
            nome= 'Cidade fictícia',
            meta = 'meta da cidade fictícia',
            texto_descritivo="texto fictício",
            preco= 1000,
        )
        
        self.objeto_url = reverse('Destinos-list') + f'{self.destino.id}/'
    
    def test_requisicao_get_para_listar_destinos(self):
        '''Teste para verificar a requisição GET para listar os destinos'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_destino(self):
        '''Teste para verificar a requisição POST para criar um destino'''

        data = {
            'foto_1': '',
            'foto_2': '',
            'nome': 'Rio de Janeiro',
            'meta' : 'Essa é um meta dado',
            'texto_descritivo':'texto descrevendo o destino',
            'preco': 1000
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_destino(self):
        """Teste para atualizar destino"""
        data = {
            'id': self.destino.id,
            'foto_1': '',
            'foto_2': '',
            'nome':'São Paulo',
            'meta' : 'Meta',
            'texto_descritivo':'texto que descreve o destino',
            'preco':105
        }
        response = self.client.put(self.objeto_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_destino(self):
        """Teste para deletar destino"""
        response = self.client.delete(self.objeto_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)