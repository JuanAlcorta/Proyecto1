from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django Equipo Coder")

def segundaVista(request):
    return HttpResponse("<br><br> Practicando una segunda vista")

def miNombreEs(self, nombre):
    data= f"Mi nombre es: <h1>{nombre}<h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Derick"
    apellido = "Carcamo"
    diccionario = {"nombre":nombre,"apellido":apellido}
    miHtml = open ("D:\PythonCurso\PhytonProyecto1\Proyecto1\Proyecto1\Plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext= Context(diccionario)
    documento= plantilla.render(miContext)
    return HttpResponse(documento)
    

  


