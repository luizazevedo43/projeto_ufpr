from django.urls import path
from catalogo.views import index, imagemfp, imagemlg, buscar, filtro
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagemfp/<int:doc_id>', imagemfp, name='imagemfp'),
    path('imagemlg/<int:doc_id>', imagemlg, name='imagemlg'),
    path('buscar/', buscar, name="buscar"),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]

    