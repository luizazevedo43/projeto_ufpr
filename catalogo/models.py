from django.db import models
from django.contrib.auth.models import User


# Montando os dados necessarios para a catalogacao de um documento 
class DocumentoFP(models.Model):

    OPCOES_CATEGORIA = [
        ("FICHA PRIMARIA", "Ficha Primária"),
        ("LEGISLACAO", "Legislação"),
        ("LIVRO", "Livro"),
    ]

    numero = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=50, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    remetente = models.TextField(null=False, blank=False)
    destinatario = models.TextField(null=False, blank=False)
    data = models.CharField(max_length=10, null=False, blank=False)
    referencia = models.CharField(max_length=100, null=False, blank=False)
    assunto = models.TextField(null=False, blank=False)
    palavras_chave = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='FICHA PRIMARIA')
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="usuariofp"
    )

    def __str__(self):
        return f"Documento [numero={self.numero}]"
    
class DocumentoLG(models.Model):

    OPCOES_CATEGORIA = [
        ("FICHA PRIMARIA", "Ficha Primária"),
        ("LEGISLACAO", "Legislação"),
        ("LIVRO", "Livro"),
    ]


    entidade_origem = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=50, null=False, blank=False)
    data = models.CharField(max_length=10, null=False, blank=False)
    ementa = models.TextField(null=False, blank=False, default=None) #Talvvez seja opcional
    assinatura = models.TextField(null=False, blank=False)
    assunto = models.TextField(null=False, blank=False, default=None) #Talvez seja opcional
    referencia =models.CharField(max_length=100, null=False, blank=False)
    local =models.CharField(max_length=100, null=False, blank=False)
    palavras_chave = models.CharField(max_length=100, null=False, blank=False)
    responsavel = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='LEGISLACAO')
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="usuariolg"
    )

    def __str__(self) -> str:
        return f"Documento [numero={self.numero}]"
    
    