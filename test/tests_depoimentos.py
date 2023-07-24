from rest_framework.test import APITestCase
from apps.viagens.models import Depoimento
from django.urls import reverse
from rest_framework import status

class DepoimentoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Depoimentos-list')
        self.depoimento = Depoimento.objects.create(
            foto='',
            depoimento= 'Depoimento teste',
            nome= 'Teste 1',
        )
        
        self.objeto_url = reverse('Depoimentos-list') + f'{self.depoimento.id}/'
    
    def test_requisicao_get_para_listar_depoimentos(self):
        '''Teste para verificar a requisição GET para listar os depoimentos'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_requisicao_post_para_criar_depoimeito(self):
        '''Teste para verificar a requisição POST para criar um depoimento'''

        data = {
            'foto': '',
            'depoimento': 'teste 3',
            'nome': 'Nome teste 3'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_depoimento(self):
        """Teste para atualizar depoimento"""
        data = {
            'id': self.depoimento.id,
            'foto':'',
            'depoimento':'Depoimento teste atualizado',
            'nome':'Teste atualizado'
        }
        response = self.client.put(path=self.objeto_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_depoimento(self):
        """Teste para deletar depoimento"""
        response = self.client.delete(self.objeto_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)