from django.contrib import admin
from catalogo.models import DocumentoFP
from catalogo.models import DocumentoLG


class ListandoDocumento(admin.ModelAdmin):

    list_display = ("id", "numero", "data", "categoria")
    list_display_links = ("id", "numero")
    search_fields = ("id", "numero",)
    list_per_page = 10

admin.site.register(DocumentoFP, ListandoDocumento)
admin.site.register(DocumentoLG, ListandoDocumento)
