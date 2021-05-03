from django.shortcuts import render
from django.http import HttpResponse
from xml.dom import minidom
from . import Funciones as Fun

# Create your views here.
def Login(request):
    return render(request,'login.html')

def Principal(request):
    direA=request.GET["Direccion_AE"]
    archivo = open(direA,encoding="utf8")
    mensaje = archivo.read()
    archivo.close()
    Fun.separacion(str(direA))
    return render(request,'principal.html',{"texto1":mensaje})


