from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=(100))
    email = models.CharField('email', max_length=(50))
    telefone = models.CharField('telefone', max_length=(25))

    def __str__(self):
        return self.nome


class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=(50))




class Avaliador(Pessoa):
    curriculo = models.CharField('curriculo', max_length=(50))

    def __str__(self):
        return self.curriculo


class Artigos(models.Model):
    titulo = models.CharField('titulo', max_length=(150))
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):
    qualidadeTecnica = models.DecimalField(decimal_places=1, max_digits=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    inovacao = models.DecimalField(decimal_places=1, max_digits=1)
    resultados = models.DecimalField(decimal_places=1, max_digits=1)
    metodologia = models.DecimalField(decimal_places=1, max_digits=1)
    adequacaoTematicaEvento = models.DecimalField(decimal_places=1, max_digits=1)
    nota = models.DecimalField(decimal_places=1, max_digits=1)   
    artigo = models.ForeignKey(Artigos, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE)

