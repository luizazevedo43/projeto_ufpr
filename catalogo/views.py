from django.shortcuts import render, get_object_or_404
from catalogo.models import DocumentoFP, DocumentoLG
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    documentofp = list(DocumentoFP.objects.all())
    documentolg = list(DocumentoLG.objects.all())

    zippedItems = documentofp + documentolg
    context = {'zippedItems': zippedItems, 'documentofp': documentofp, 'documentolg': documentolg}

    return render(request, 'catalogo/index.html', context)



def imagemfp(request, doc_id):
    item = get_object_or_404(DocumentoFP, pk=doc_id)
    return render(request, 'catalogo/imagemfp.html', {"item": item})

def imagemlg(request, doc_id):
    item = get_object_or_404(DocumentoLG, pk=doc_id)
    return render(request, 'catalogo/imagemlg.html', {"item": item})


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
            
    #all_docs = documento1 + documento2
    #p = Paginator(all_docs, 10) 


    return render(request, "catalogo/buscar.html", {"cards":documento1, "cardslg":documento2})

def filtro(request, categoria):
    if categoria == "FICHA PRIMARIA":
        documentofp = list(DocumentoFP.objects.all())
        documentolg = []
        zippedItems = documentofp + documentolg
        context = {'documentofp':documentofp, 'zippedItems':zippedItems, 'documentolg':documentolg}
        
    if categoria == "LEGISLACAO":
        documentolg = list(DocumentoLG.objects.all())
        documentofp = []
        zippedItems = documentofp + documentolg
        context = {'documentofp':documentofp, 'zippedItems':zippedItems, 'documentolg':documentolg}


    return render(request, 'catalogo/index.html', context)