from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Diretor(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome")
    nascimento = models.DateField("Data de nascimento", default=dt.now(),
                                  help_text="Data de nascimento.")
    falecimento = models.DateField("Data de falecimento", default=dt.now(), null=True,
                                  blank=True,
                                  help_text="Data de falecimento (caso esteja vivo, deixe em branco).")
    nacionalidade = models.CharField(max_length=255)

    OPCOES_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não-binário'),
    )

    id_genero = models.CharField("Identidade de gênero", max_length=1,
                                  choices=OPCOES_GENERO, default='M')

    class Meta:
        ordering = ['nome', 'nascimento']

    def __str__(self):
        return self.nome

    def buscar_url(self):
        return reverse('sobre-diretor', args=[str(self.id)])

class Ator(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome artistico")
    nascimento = models.DateField("Data de nascimento", default=dt.now(),
                                       help_text="Data de nascimento")
    falecimento = models.DateField("Data de falecimento", default=dt.now(), null=True,
                                   blank=True,
                                   help_text="Data de falecimento (caso esteja vivo, deixe em branco).")
    nacionalidade = models.CharField(max_length=255)

    OPCOES_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não-binário'),
    )

    id_genero = models.CharField("Identidade de gênero", max_length=1,
                                  choices=OPCOES_GENERO, default='M')

    class Meta:
        ordering = ['nome', 'nascimento']

    def __str__(self):
        return self.nome

    def buscar_url(self):
        return reverse('sobre-ator', args=[str(self.id)])

class Genero(models.Model):
    titulo = models.CharField("Genero", max_length=255, help_text="Nome do genero")

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Filme(models.Model):
    titulo = models.CharField(max_length=280, help_text="Título do filme")
    sinopse = models.TextField(help_text="Sinopse")
    genero = models.ManyToManyField(Genero, related_name="filmes")
    data = models.DateField(default=dt.now(), help_text="Data de estreia")
    diretor = models.ForeignKey(Diretor, on_delete=models.SET_NULL, null=True,
                                 help_text="Diretor")
    elenco = models.ManyToManyField(Ator, related_name="filmes")

    class Meta:
        ordering = ['titulo', 'data']

    def __str__(self):
        return f"{self.titulo} - {self.data}"

    def buscar_url(self):
        return reverse('sobre-filme', args=[str(self.id)])

    def mostrar_genero(self):
        return ', '.join(genero.titulo for genero in self.genero.all()[:3])

    mostrar_genero.short_description = 'Genero'
