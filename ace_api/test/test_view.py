from django.test import TestCase
from django.urls import reverse

class AceListTest(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class IndiceTest(TestCase):

    def test_status_code_200(self):
        ciclo = 1
        response = self.client.get(reverse('indice', args=(ciclo,)))
        self.assertEqual(response.status_code, 200)


class MapaTest(TestCase):

    def test_status_code_200(self):
        ciclo = 1
        response = self.client.get(reverse('mapa', args=(ciclo,)))
        self.assertEqual(response.status_code, 200)

        