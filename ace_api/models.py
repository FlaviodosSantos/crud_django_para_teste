from django.db import models

# Create your models here.


class Ace(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=6)
    zona = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


def is_prime(num):

    if num > 1:

       for i in range(2, num):
           if (num % i) == 0:
               return False
       else:
           return True

    else:
       return False
