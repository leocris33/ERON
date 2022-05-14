from django.shortcuts import redirect, render
from ast import Num, Return
from django.http import HttpResponse, JsonResponse
from .forms import visitanteForm
from mainSistema.models import Dispositivos, Niveles_seguridad, Permiso, Visitante
from urllib import response
# Create your views here.


def inicio(request):
    return render(request,"index.html")

def visitante(request):
    return render(request,"layouts/visitante.html")


def visualizarVisitante(request):
    return render(request,"layouts/visualizarVisi.html")

def ingreso(request):
    return render(request,'layouts/ingreso.html')

def dispositivos(request):
    return render(request,"layouts/dispositivos.html")

def puntos_de_control(request):
    return render(request,"layouts/puntos_de_control.html")

def permiso(request):
    return render(request,"layouts/permiso.html")

def reporte_permiso(request):
    datosPermiso = Permiso.objects.all()
    return render(request,"layouts/reporte_permiso.html",{
        'mostrarPermiso' : datosPermiso
    
     })
  
    
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


# def pruebas_DB(request,nombre,apellidos,documento,fecha_nac,cargo,organizacion,permiso):
  

#     nuevo_visit = Visitante(
#         nombre = nombre,
#         apellido = apellidos,
#         documento = documento,
#         fechaNacimiento = fecha_nac,
#         cargo = cargo,
#         organizacion = organizacion,
#         permiso = permiso
    
        
#     )

#     nuevo_visit.save()
   
#     return HttpResponse(f"El visitante {nuevo_visit.nombre} ha sido guardado")





def save_visitante(request):

    if request.method == 'POST':
        nombre = request.POST["nombres"]
        apellido = request.POST["apellidos"]
        documento = request.POST["documento"]
        fecha_nac = request.POST["fecha_nac"]
        cargo = request.POST["cargo"]
        organizacion = request.POST["organizacion"]
        permiso = request.POST["permiso"]
        imagen = request.POST["imagen"]



        visit = Visitante(

            nombre = nombre,
            apellido = apellido,
            documento = documento,
            fechaNacimiento = fecha_nac,
            cargo = cargo,
            organizacion = organizacion,
            permiso = permiso,
            imagen = imagen


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

def save_permiso(request):

    if request.method == 'POST':
        fecha_inicio = request.POST["fecha_inicio"]
        fecha_fin = request.POST["fecha_fin"]
        objetos = request.POST["objetos"]
        autorizacion = request.POST["autorizacion"]
        
   


        permit = Permiso(

            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            objetos = objetos,
            autorizacion = autorizacion,
           


        )
        permit.save()

        return redirect("permiso")
    
    else:
        return redirect("inicio")

def save_dispositivos(request):

    if request.method == 'POST':
        nombre = request.POST["nombre"]
        direccion_ip = request.POST["direccion_ip"]
        direccion_mac = request.POST["direccion_mac"]
        identificador = request.POST["identificador"]
        ubicacion = request.POST["ubicacion"]
        
   


        dispo = Dispositivos(

            nombre = nombre,
            direcion_ip = "",
            direcion_mac = direccion_mac,
            identificador = identificador,
            ubicacion = ubicacion,
           


        )
        dispo.save()

        return redirect("dispositivos")
    
    else:
        return redirect("inicio")

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

def editar(request,id):
    visitante = Visitante.objects.get(id=id)
    return render(request, 'layouts/editar.html')

def eliminar(request):
    visitante = Visitante.objects.get(id=id)
    visitante.delete()
    return render(request, 'layouts/eliminar.html')






