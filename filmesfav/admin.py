from django.contrib import admin
from .models import Filme, Diretor, Ator, Genero

# Register your models here.

admin.site.register(Genero)

class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento', 'falecimento')
    fields = ['nome', ('nascimento', 'falecimento',), 'nacionalidade', 'id_genero']

admin.site.register(Ator, AtorAdmin)

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'mostrar_genero')

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento', 'falecimento')
    fields = ['nome', ('nascimento', 'falecimento',), 'nacionalidade', 'id_genero']
