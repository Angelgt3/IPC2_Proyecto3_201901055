from django.shortcuts import render
from django.http import HttpResponse
from xml.dom import minidom
from . import Funciones as Fun

# Create your views here.
def Login(request):
    return render(request,'login.html')

def Consu(request):
    try:
        archivo = open("estadistica.xml",encoding="utf8")
        mensaje = archivo.read()
        archivo.close()
        return render(request,'Consulta.html',{'texto1':mensaje})
    except:
        return render(request,'Consulta.html')
    

def Principal(request):
    if request.GET["Direccion_AE"]:
        try:
            ruta=request.GET["Direccion_AE"]
            archivo = open(ruta,encoding="utf8")
            mensaje = archivo.read()
            archivo.close()
            Fun.separacion(str(ruta))
            archivo = open("estadistica.xml",encoding="utf8")
            mensaje2 = archivo.read()
            archivo.close()
        except:         
            return render(request,'login.html')
        return render(request,'principal.html',{"texto1":mensaje,"texto2":mensaje2})
    else:
        return render(request,'login.html')

def Info(request):
    return render(request,'Infomacion.html')

def Doc(request):
    Fun.doc()
    return render(request,'Consulta.html')

def Filtros(request):
    try:
        fecha=request.GET["ffecha"]
        archivo = open("estadistica.xml",encoding="utf8")
        mensaje2 = archivo.read()
        usuarios=Fun.filtrar(fecha)
        archivo.close()
        return render(request,'Filtros.html',{'fecha':fecha,'usuario':usuarios})    
    except:
        return render(request,'principal.html')

def Filtro2(request):
    try:
        codigo=request.GET["otro"]
        archivo = open("estadistica.xml",encoding="utf8")
        mensaje2 = archivo.read()
        fechas=Fun.fil(codigo)
        archivo.close()
        return render(request,'FiltroC.html',{'fecha':fechas,'codigo':codigo})    
    except:
        return render(request,'principal.html')    
    





