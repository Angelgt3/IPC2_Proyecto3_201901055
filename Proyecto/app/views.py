from django.shortcuts import render
from django.http import HttpResponse
from xml.dom import minidom
from . import Funciones as Fun

# Create your views here.
def Login(request):
    return render(request,'login.html')

def Principal(request):
    ruta=request.GET["Direccion_AE"]
    archivo = open(ruta,encoding="utf8")
    mensaje = archivo.read()
    archivo.close()
    Fun.separacion(str(ruta))
    archivo = open("estadistica.xml",encoding="utf8")
    mensaje2 = archivo.read()
    archivo.close()
    return render(request,'principal.html',{"texto1":mensaje,"texto2":mensaje2})





