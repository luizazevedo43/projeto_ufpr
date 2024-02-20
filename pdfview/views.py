from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from catalogo.models import DocumentoFP, DocumentoLG

def renderiza_doc_pdf_fp(request, *args, **kwargs):

    pk = kwargs.get('pk')
    documento = get_object_or_404(DocumentoFP, pk=pk)

    template_path = 'catalogo/pdf_view_fp.html'
    contexto = {'documento': documento}
    resposta = HttpResponse(content_type='application/pdf')
    resposta['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(contexto)

    pisa_status = pisa.CreatePDF(
        html, dest=resposta
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return resposta

def renderiza_doc_pdf_lg(request, *args, **kwargs):

    pk = kwargs.get('pk')
    documento = get_object_or_404(DocumentoLG, pk=pk)

    template_path = 'catalogo/pdf_view_lg.html'
    contexto = {'documento': documento}
    resposta = HttpResponse(content_type='application/pdf')
    resposta['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(contexto)

    pisa_status = pisa.CreatePDF(
        html, dest=resposta
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return resposta


                            
