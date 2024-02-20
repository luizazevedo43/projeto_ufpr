from django.shortcuts import render, get_object_or_404
from catalogo.models import DocumentoFP, DocumentoLG
from django.db.models import Q


def index(request):
    documento1 = DocumentoFP.objects.all()
    documento2 = DocumentoLG.objects.all()
    return render(request, 'catalogo/index.html', {"cards": documento1, "cardslg":documento2})


def imagemfp(request, doc_id):
    documento = get_object_or_404(DocumentoFP, pk=doc_id)
    return render(request, 'catalogo/imagemfp.html', {"documento": documento})

def imagemlg(request, doc_id):
    documento = get_object_or_404(DocumentoLG, pk=doc_id)
    return render(request, 'catalogo/imagemlg.html', {"documento": documento})

def buscar(request):
    documento1 = DocumentoFP.objects.all()
    documento2 = DocumentoLG.objects.all()

    if "buscar" in request.GET:
        nome_a_buscar = request.GET.get('buscar')
        if nome_a_buscar:
            documento1 = documento1.filter(Q(palavras_chave__icontains=nome_a_buscar) | Q(data__icontains=nome_a_buscar) | Q(numero__icontains=nome_a_buscar)
                            | Q(titulo__icontains=nome_a_buscar) | Q(remetente__icontains=nome_a_buscar) | Q(destinatario__icontains=nome_a_buscar)
                            | Q(referencia__icontains=nome_a_buscar) | Q(assunto__icontains=nome_a_buscar)).distinct()
            
            documento2 = documento2.filter(Q(palavras_chave__icontains=nome_a_buscar) | Q(entidade_origem__icontains=nome_a_buscar) | Q(data__icontains=nome_a_buscar)
                            | Q(ementa__icontains=nome_a_buscar) | Q(assinatura__icontains=nome_a_buscar) | Q(assunto__icontains=nome_a_buscar)
                            | Q(referencia__icontains=nome_a_buscar) | Q(local__icontains=nome_a_buscar) | Q(responsavel__icontains=nome_a_buscar)).distinct()


    return render(request, "catalogo/buscar.html", {"cards":documento1, "cardslg":documento2})

def filtro(request, categoria):
    if categoria == "FICHA PRIMARIA":
        documento = DocumentoFP.objects.all()
        context = {'cards':documento}
    if categoria == "LEGISLACAO":
        documento = DocumentoLG.objects.all()
        context = {'cardslg':documento}

    return render(request, 'catalogo/index.html', context)