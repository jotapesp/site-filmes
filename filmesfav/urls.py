from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("filmesfav/filme/<id>", views.filme, name='sobre-filme'),
    path("filmesfav/elenco/<id>", views.ator, name='sobre-ator'),
    path("filmesfav/diretores/<id>", views.diretor, name='sobre-diretor'),
]
