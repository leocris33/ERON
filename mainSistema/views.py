from datetime import datetime, timezone
from django.shortcuts import redirect, render
from ast import Num, Return
from django.http import HttpResponse, JsonResponse
from .forms import visitanteForm
from mainSistema.models import Alerta, Dispositivos, Niveles_seguridad, Permiso, Punto_control, Visitante, Ingreso, Punto_control_Dispositivos
from urllib import response
from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO

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




def inf_visitante(request):

    return render(request,"layouts/inf_visitante.html")



def dispositivos(request):
    return render(request,"layouts/dispositivos.html")

def puntos_de_control(request):
    return render(request,"layouts/puntos_de_control.html")

def permiso(request, id):
    datosVisitante = Visitante.objects.get(id = id)
    niveles_seg = Niveles_seguridad.objects.all()
    return render(request,"layouts/permiso.html",{
        'mostrarVisi'   : datosVisitante,
        'niveles'       : niveles_seg
        
    })







def reporte_permiso(request):
    datosPermiso = Permiso.objects.all().values('id','idVisitante_permi__documento', 'fecha_inicio', 'fecha_fin', 'objetos', 'autorizacion' )
    visi = Visitante.objects.all()
    datoid = Niveles_seguridad.objects.all()


    
    return render(request,"layouts/reporte_permiso.html",{ 
        'documentoVisi'  : visi,    
        'mostrarPermiso' : datosPermiso,
        'mostrarID'      : datoid 
     })

    # return JsonResponse({
    #     'dato' : list(datosPermiso)
    # }, status=200)


def reporte_puntos_de_control(request):
    datos = Punto_control.objects.all()
    return render(request,"layouts/reporte_puntos_de_control.html",{
        'mostrarPunto' : datos

    })

def reporte_dispositivos(request):
    datos = Dispositivos.objects.all()
    return render(request,"layouts/reporte_dispositivos.html",{
        'mostrarDis' : datos

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

def save_puntos_de_control(request):

    if request.method == 'POST':
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        


        punto = Punto_control(

            nombre = nombre,
            descripcion = descripcion,
          


        )
        punto.save()

        return redirect("puntos_de_control")
    
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
        
        pk = request.POST["pk"]
        fecha_inicio = request.POST["fecha_inicio"]
        fecha_fin = request.POST["fecha_fin"]
        objetos = request.POST["objetos"]
        nivel_seg = request.POST["nivel_seg"]
        autorizacion = request.POST["autorizacion"]

        visit = Visitante.objects.get(pk = int(pk))
        nivel_s = Niveles_seguridad.objects.get(pk = int(nivel_seg))
        
   


        permit = Permiso(

            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            objetos = objetos,
            autorizacion = autorizacion,
            idVisitante_permi = visit,
            idNiveles_seguridad = nivel_s
        )
        
        permit.save()

        return redirect("reporte_permiso")

        
    
    else:
        #return redirect("inicio")
        return JsonResponse({
            'error' : 'algo está mal'

        }, status=400)

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

def alertas(request,id,obs):    
    Alert = Alerta(
     dispositivos_idDispositivos_id = id,
     fecha = datetime.now(),
     observaciones = obs,
    )
    Alert.save()
    return redirect("inicio")
    #id = Dispositivos.objects.get(id=id).values()
    #observaciones= Alerta.objects.get(obs=obs).values()
    # return render(request,"layouts/alertas.html",{
    #     'alertas': datos

    # })
    
    # return JsonResponse({
    #     'datos' : list(info),
    # }, status=200)

def qr(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "generarQR.html", context=context)






