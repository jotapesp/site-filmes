from django.shortcuts import render
from .models import Filme, Ator, Genero, Diretor
from django.views import generic

# Create your views here.
def home(request):
    filmes = Filme.objects.all()
    context = {"filmes": filmes}
    return render(request, "home.html", context)

def filme(request, id):
    filme = Filme.objects.get(pk=id)

    context = {"filme": filme}
    return render(request, "filme.html", context)

def ator(request, id):
    ator = Ator.objects.get(pk=id)
    genero = 'Não-binário'
    if ator.id_genero == 'M':
        genero = 'Masculino'
    elif ator.id_genero == 'F':
        genero = 'Feminino'

    context = {"ator": ator, "genero": genero}
    return render(request, "ator.html", context)

def diretor(request, id):
    diretor = Diretor.objects.get(pk=id)
    genero = 'Não-binário'
    if diretor.id_genero == 'M':
        genero = 'Masculino'
    elif diretor.id_genero == 'F':
        genero = 'Feminino'

    context = {"diretor": diretor, "genero": genero}
    return render(request, "diretor.html", context)
