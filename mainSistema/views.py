from django.shortcuts import redirect, render
from ast import Num, Return
from django.http import HttpResponse, JsonResponse
from .forms import visitanteForm
from mainSistema.models import Dispositivos, Niveles_seguridad, Permiso, Visitante, Ingreso, Punto_control_Dispositivos
from urllib import response
# Create your views here.


def inicio(request):
    return render(request,"index.html")

def visitante(request):
    return render(request,"layouts/visitante.html")


def visualizarVisitante(request):
    datovisit = Visitante.objects.all()
    return render(request,"layouts/visualizarVisi.html",{
    'mostrarvist' : datovisit
})

def editarVisitante(request, id):
    visitante = Visitante.objects.get(id=id)
    modelo = visitanteForm(request.POST or  None, request.Files or None ,instance=visitante)
    if modelo.is_valid() and request.POST:
        modelo.save()
        return redirect("visitante")
    return render(request, "layouts/editar_visitante.html", {
        'editarvisitante' : visitante
    })


def inf_visitante(request):

    return render(request,"layouts/inf_visitante.html")



def dispositivos(request):
    return render(request,"layouts/dispositivos.html")

def puntos_de_control(request):
    return render(request,"layouts/puntos_de_control.html")

def permiso(request):
    return render(request,"layouts/permiso.html")







def reporte_permiso(request):
    datosPermiso = Permiso.objects.all().values('id','idVisitante_permi__documento', 'fecha_inicio', 'fecha_fin', 'objetos', 'autorizacion' )
    visi = Visitante.objects.all()


    
    return render(request,"layouts/reporte_permiso.html",{ 
        'documentoVisi'  : visi,    
        'mostrarPermiso' : datosPermiso
     })

    # return JsonResponse({
    #     'dato' : list(datosPermiso)
    # }, status=200)







  
    
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




# Funcion para guardar lo ingresos a puntos de control
def ingreso(request, documento, id_disp):

    id_permiso = Permiso.objects.filter(idVisitante_permi__documento = documento).values('id')
    id_pto_ctrl = Punto_control_Dispositivos.objects.filter(idDispositivos = id_disp).values('idPunto_control_dispo')

    #id_permiso = get_id_permiso(documento)
   

    return JsonResponse({
        'id_permiso'    : list(id_permiso),
        'id_disp'       : list(id_pto_ctrl)
    }, status=200)


def listado_ingresos(request):
    tittle = 'Listado ingresos'

    return render(request, 'layouts/listado_ingresos.html', {
        'tittle'    : tittle
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
            direcion_ip = direccion_ip,
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


def get_Visitante (request, documento):
    try:
        Visitante = Visitante.objects.filter(documeto=documento)
        response = f"el visitante solicitado es : {Visitante.nombre }{Visitante.apellido}{Visitante.documento}{Visitante.permiso}{Visitante.cargo}{Visitante.organizacion}{Visitante.fechaNacimiento}{Visitante.imagen}"
    except:
        response = "el visitante no existe"

    return HttpResponse (Visitante)


def editar(request,id):
    visitante = Visitante.objects.get(id=id)
    return render(request, 'layouts/editar.html')

def eliminar(request):
    visitante = Visitante.objects.get(id=id)
    visitante.delete()
    return render(request, 'layouts/eliminar.html')






