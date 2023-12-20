from django.test import TestCase
from .models import Ace, is_prime


class AceTestCase(TestCase):

    def setUp(self):
        Ace.objects.create(
            nome='Antonio',
            matricula=14666,
            zona=3
        )

    def test_retorno_str(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.__str__(), 'Antonio')

    def test_matricula(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.matricula, '14666')

    def test_zona(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertEquals(ace.zona, 3)

    def test_is_active(self):
        ace = Ace.objects.get(nome='Antonio')
        self.assertTrue(ace.is_active)



class CalculatorTest(TestCase):

    def test_nonprime(self):
        self.assertEqual(is_prime(12), False)

    def test_prime(self):
        self.assertEqual(is_prime(19), True)

    def test_invalid(self):
        self.assertEqual(is_prime(-1), False)

