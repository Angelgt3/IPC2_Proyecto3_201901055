import xml.etree.cElementTree as ET
import webbrowser
from xml.dom import minidom

def doc():
    try:
        nombreArchivo = 'C:/Users/angge/OneDrive/Documentos/GitHub/IPC2_Proyecto3_201901055/Documentacion/Documentacion_IPC2_Proyecto3.pdf'
        webbrowser.open_new_tab(nombreArchivo)
    except:
        print("no se pudo abrir")

def fil(cod):
    fechas=list()
    doc = minidom.parse("estadistica.xml")
    estadisticas=doc.getElementsByTagName("ESTADISTICA")
    for esta in estadisticas:
        fecha=esta.getElementsByTagName("FECHA")[0].firstChild.data
        errores=esta.getElementsByTagName("ERORRES")
        for er in errores:
            error=er.getElementsByTagName("ERROR")
            for e in error:
                #fechas.append(e.getElementsByTagName("CODIGO")[0].firstChild.data)
                if cod==e.getElementsByTagName("CODIGO")[0].firstChild.data:
                    fechas.append(fecha)
    return fechas


def filtrar(fe):
    linea=list()
    doc = minidom.parse("estadistica.xml")
    estadisticas=doc.getElementsByTagName("ESTADISTICA")
    for esta in estadisticas:
        if fe == esta.getElementsByTagName("FECHA")[0].firstChild.data:
            report=esta.getElementsByTagName("REPORTADO_POR") 
            for re in report:
                usuario=re.getElementsByTagName("USUARIO")
                for u in usuario:
                    linea.append(u.getElementsByTagName("EMAIL")[0].firstChild.data)
                    #linea.append(u.getElementsByTagName("CANTIDAD_MENSAJES")[0].firstChild.data)               
            return linea
    return None
            
            
def separacion(ruta):
    eventos=list()
    estoy=False
    lineas=list()
    archivo = open(ruta, encoding="utf8")
    for linear in archivo:
        lineal=linear.rstrip()
        linea=lineal.lstrip()
        if linea=="<EVENTO>":
        	estoy=True
        elif linea=="</EVENTO>":
            estoy=False
            temp=[]
            for i in lineas:
                temp.append(i)
            eventos.append(temp)
            for l in range(len(lineas)):
                lineas.pop()
			#print(f"vector lineas {lineas}")
			#print(f"vector eventos {eventos}")
        elif estoy==True:
        	lineas.append(linea)

    Datos_Dia=list()
    Datos=list()

    for e in eventos:
        contador=0
        for l in e:
            if contador==0:
                fechar=l.split(",")
                fechal=fechar[1].rstrip()
                fecha=fechal.lstrip()
                #print(f"fecha: {fecha}")
                Datos_Dia.append(fecha)
                contador+=1
            elif contador==1:
                repot1=l.split('"')
                repot2=repot1[2].split(">")
                reportado=repot2[0].lstrip()
                #print(f"Reportado: {reportado}")
                Datos_Dia.append(reportado)
                contador+=1
            elif contador==2:
                l2=l.replace("<","")
                l3=l2.replace(">","")
                l4=l3.split(":")
                l5=l4[1].split(",")
                Afectados=[]
                for i in l5:
                    #print(f"Afectados: {i}")
                    Afectados.append(i)
                Datos_Dia.append(Afectados)
                contador+=1
            elif contador==3:
                l2=l.split(":")
                l3=l2[1].split("-")
                codigo=l3[0]
                #print(f"Codigo: {codigo}")
                Datos_Dia.append(codigo)
                contador+=1
                temp=[]
                for i in Datos_Dia:
                    temp.append(i)
                Datos.append(temp)
                for l in range(len(Datos_Dia)):
                    Datos_Dia.pop()
    
    
    estadisticas =ET.Element("ESTADISTICAS")
    estadisticas.text="\n\t"

    while True:
        estadistica = ET.SubElement(estadisticas, "ESTADISTICA")
        estadistica.text="\n\t\t"
        
        posiciones=list()
        ya=list()
        for t in range(len(Datos)):
            if Datos[0][0]==Datos[t][0]:
                    posiciones.append(t)
        

        valor=Datos[posiciones[0]][0]
        Fecha = ET.SubElement(estadistica,"FECHA")
        Fecha.text=valor
        Fecha.tail="\n\t\t"
        Sumatoria = ET.SubElement(estadistica,"CANTIDAD_MENSAJES")
        Sumatoria.text=str(len(posiciones))
        Sumatoria.tail="\n\t\t"
        Reportes = ET.SubElement(estadistica,"REPORTADO_POR")
        Reportes.text="\n\t\t\t"
        Reportes.tail="\n\t\t"
        
        te=list()
        for b in posiciones:
            te.append(Datos[b][1])
        while True:
            correo=te[0]
            cantidad=te.count(correo)
            Usuario= ET.SubElement(Reportes,"USUARIO")
            Usuario.text="\n\t\t\t\t" 
            Email= ET.SubElement(Usuario,"EMAIL")
            Email.text=correo
            Email.tail="\n\t\t\t\t"
            C_Mensaje=ET.SubElement(Usuario,"CANTIDAD_MENSAJES")
            C_Mensaje.text=str(cantidad)
            C_Mensaje.tail="\n\t\t\t"

            co=0
            for r in range(len(te)):
                if te[co]==correo:
                    te.pop(co)
                    co-=1
                co+=1
            if len(te)==0:
                Usuario.tail="\n\t\t"
                break
            else:
                Usuario.tail="\n\t\t\t"

        Afectados = ET.SubElement(estadistica,"AFECTADOS")
        Afectados.text="\n\t\t\t"
        Afectados.tail="\n\t\t"
        te2=list()
        for b in posiciones:
            for a in Datos[b][2]:
                te2.append(a) 
        while True:
            afe=te2[0]
            Afectado= ET.SubElement(Afectados,"AFECTADO")
            Afectado.text=f"{afe}"
            c=0
            for f in range(len(te2)):
                if te2[c]==afe:
                    te2.pop(c)
                    c-=1
                c+=1
            
            if len(te2)==0:
                Afectado.tail="\n\t\t"
                break
            else:
                Afectado.tail="\n\t\t\t"

        Errores = ET.SubElement(estadistica,"ERORRES")
        Errores.text="\n\t\t\t"
        Errores.tail="\n\t"

        te3=list()
        for b in posiciones:
            te3.append(Datos[b][3])
        while True:
            cod=te3[0]
            cantidad=te3.count(cod)
            Error= ET.SubElement(Errores,"ERROR")
            Error.text="\n\t\t\t\t" 
            Codigo= ET.SubElement(Error,"CODIGO")
            Codigo.text=cod
            Codigo.tail="\n\t\t\t\t"
            Cantidad= ET.SubElement(Error,"CANTIDAD_MENSAJES")
            Cantidad.text=str(cantidad)
            Cantidad.tail="\n\t\t\t"
            co=0
            for r in range(len(te3)):
                if te3[co]==cod:
                    te3.pop(co)
                    co-=1
                co+=1
            if len(te3)==0:
                Error.tail="\n\t\t"
                break
            else:
                Error.tail="\n\t\t\t"

        tamaño=len(Datos)
        cont=0
        for r in range(tamaño):
            if Datos[cont][0]==valor:
                Datos.pop(cont)
                cont-=1
            cont+=1
        
        if len(Datos)==0:
            estadistica.tail="\n"
            break
        else:
            estadistica.tail="\n\t"


    Arbol=ET.ElementTree(estadisticas)
    Arbol.write("estadistica.xml")
    