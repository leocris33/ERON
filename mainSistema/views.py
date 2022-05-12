from django.shortcuts import redirect, render
from ast import Num, Return
from django.http import HttpResponse, JsonResponse
from .forms import visitanteForm
from mainSistema.models import Niveles_seguridad, Visitante
from urllib import response
# Create your views here.


def inicio(request):
    return render(request,"index.html")

def visitante(request):
    return render(request,"layouts/visitante.html")


def ingreso(request):
    return render(request,'layouts/ingreso.html')

def dispositivos(request):
    return render(request,"layouts/dispositivos.html")

def puntos_de_control(request):
    return render(request,"layouts/puntos_de_control.html")

def permiso(request):
    return render(request,"layouts/permiso.html")

def reporte_visitante(request):
    datos = Visitante.objects.all()
    return render(request,"layouts/reporte_visitante.html",{
        'mostrarVisitante' : datos

    })

def generar_QR(request):
    return render(request,"layouts/generarQR.html")

def niveles_seguridad(request):
    return render(request,"layouts/niveles_seguridad.html")
        



def crear_nivel_seguridad(request):
    return render(request, "layouts/crear_nivel_seguridad.html")

def administrar_niveles(request):
    datoSeguridad = Niveles_seguridad.objects.all()
    return render(request,"layouts/administrar_niveles.html",{
        'niveles_seguridad' : datoSeguridad

    })


def pruebas_DB(request,nombre,apellidos,documento,fecha_nac,cargo,organizacion,permiso):
  

    nuevo_visit = Visitante(
        nombre = nombre,
        apellido = apellidos,
        documento = documento,
        fechaNacimiento = fecha_nac,
        cargo = cargo,
        organizacion = organizacion,
        permiso = permiso
    
        
    )

    nuevo_visit.save()
   
    return HttpResponse(f"El visitante {nuevo_visit.nombre} ha sido guardado")





def save_visitante(request):

    if request.method == 'POST':
        nombre = request.POST["nombres"]
        apellido = request.POST["apellidos"]
        documento = request.POST["documento"]
        fecha_nac = request.POST["fecha_nac"]
        cargo = request.POST["cargo"]
        organizacion = request.POST["organizacion"]
        permiso = request.POST["permiso"]
   


        visit = Visitante(

            nombre = nombre,
            apellido = apellido,
            documento = documento,
            fechaNacimiento = fecha_nac,
            cargo = cargo,
            organizacion = organizacion,
            permiso = permiso


        )
        visit.save()

        return redirect("visitante")
    
    else:
        return redirect("inicio")

def save_niveles_seguridad(request):

    if request.method == 'POST':
        tipo_acceso = request.POST["tipo_acceso"]
        descripcion = request.POST["descripcion"]
        


        nivel = Niveles_seguridad(

            tipo_acceso = tipo_acceso,
            descripcion = descripcion,
          


        )
        nivel.save()

        return redirect("crear_nivel_seguridad")
    
    else:
        return redirect("inicio")

def get_visitante (request):
    try:
        visitante = Visitante.objects.all
        response = f"el visitante solicitado es : {Visitante.nombre }{Visitante.apellido}"
    except:
        response = "el visitante no existe"

    return HttpResponse (Visitante)

def get_Nivel_seguridad (request):
    try:
        niveles_seguridad = Niveles_seguridad.objects.all
        response = f"el visitante solicitado es : {Niveles_seguridad.tipo_acceso }{Niveles_seguridad.descripcion}"
    except:
        response = "el visitante no existe"

    return HttpResponse (Niveles_seguridad)
    


# def save_permiso(request):

#     if request.method == 'POST':
#         nombres = request.POST["nombres"]
#         apellidos = request.POST["apellidos"]
#         documento = request.POST["documento"]
#         fecha_nac = request.POST["fecha_nac"]
#         cargo = request.POST["cargo"]
#         organizacion = request.POST["organizacion"]
#         permiso = request.POST["permiso"]
   


#         visit = Visitante(

#             nombre = nombres,
#             apellido = apellidos,
#             documento = documento,
#             fechaNacimiento = fecha_nac,
#             cargo = cargo,
#             organizacion = organizacion,
#             permiso = permiso


#         )
#         visit.save()

#         return redirect("visitante")
    
#     else:
#         return redirect("inicio"

def prueba(request):
    lista = []

    datos = Visitante.objects.all().values('nombre', 'apellido', 'documento', 'permiso', 'cargo', 'organizacion', 'fechaNacimiento', '' )
    
  
    return render(request,"reporte_visitante.html",{
         'visitante' : datos

    })

def pruebas_orm(request):

    visitas = Visitante.objects.all().values('nombre', 'apellido', 'documento')

    return JsonResponse({
        'visitantes' : list(visitas)


    }, status=200)








