from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('nicras', password='123')
    
    def test_autenticacao_user(self):
        """Teste que verifica a autenticacao de um user com credenciais corretas"""
        user = authenticate(username='nicras', password='123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_username_incorreto(self):
        """Teste que verifica username na autenticação."""
        user = authenticate(username='nic', password='123')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get(self):
        """Teste que verifica requisicoes não autorizadas (não autenticadas)."""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_requisicao_get_authuser(self):
        """Teste que verifica requisicoes autorizadas (autenticados)"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)