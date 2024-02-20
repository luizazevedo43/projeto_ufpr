from django.urls import path
from .views import renderiza_doc_pdf_fp, renderiza_doc_pdf_lg

urlpatterns = [
    path ('pdffp/<pk>/', renderiza_doc_pdf_fp, name='view_documentofp'),
    path ('pdflg/<pk>/', renderiza_doc_pdf_lg, name='view_documentolg'),
]