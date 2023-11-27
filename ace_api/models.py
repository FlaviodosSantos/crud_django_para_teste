from django.db import models

BAIRROS = [("ac", "Acampamento"), ("ad", "Adjuto Dias"), ("al", "Alto da Boa Vista"), ("br", "Barra Nova"),
           ("bp", "Boa Passagem"), ("cf", "Canutos e Filhos"), ("cb", "Castelo Branco"), ('ct', "Centro"), ("nd", "Nova Descoberta")]

TIPO_IMOVEL = [("tb", "tb"), ("out", "outros")]

CICLO_LIRA = [(1, 1), (2, 2), (3, 3), (4, 4)]

# Create your models here.
class Ace(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=6)
    zona = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome 


class Bairro(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Indice(models.Model):
    ciclo = models.IntegerField(choices=CICLO_LIRA)
    bairro_nome = models.OneToOneField(
        Bairro, related_name='bairros', unique=True, on_delete=models.DO_NOTHING)
    indice_bairro = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True, default=0)

    def __str__(self):
        indice = str(self.ciclo)+'_'+str(self.bairro_nome)
        return indice

    class Meta:
        ordering = ['bairro_nome']
