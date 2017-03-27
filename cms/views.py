from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
# Create your views here.

def barra(request):
    respuesta = "Esto es la barra,"
    respuesta += " y esto es lo que hay:"
    lista = Pages.objects.all()
    for pagina in lista:
        respuesta += '<br><a href="/page/' + str(pagina.id) + '">' + pagina.name + '</a>'

    return HttpResponse(respuesta)

def pagina(request,identificador):
    try:
        pagina = Pages.objects.get(id=identificador)
        respuesta = "Has introducido " + pagina.name + " que corresponde a: " + str(pagina.page) + " y el id es: " + str(pagina.id)
    except Pages.DoesNotExist:
        respuesta = "No existe la pagina con el identificador " + str(identificador)

    return HttpResponse(respuesta)
