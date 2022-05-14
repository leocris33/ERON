from tabnanny import verbose
from django.db import models


# Create your models here.




class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    documento = models.CharField(max_length=100, verbose_name="Documento")
    permiso = models.BooleanField(default=False, max_length=50)
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    organizacion = models.CharField(max_length=100, verbose_name="Organizacion")
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True,)
    


class Niveles_seguridad(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_acceso = models.CharField(max_length=100, verbose_name="Tipo de acceso")
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion", null=True)


class Dispositivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direcion_ip = models.CharField(max_length=100, verbose_name="Direccion IP")
    direcion_mac = models.CharField(max_length=100, verbose_name="Direccion MAC")
    identificador = models.CharField(max_length=100, verbose_name="Identificador")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicacion")

class Alerta(models.Model):
    id = models.AutoField(primary_key=True)
    idDispositivos = models.ForeignKey(Dispositivos, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(verbose_name="Fecha")
    observaciones = models.CharField(max_length=200, verbose_name="Observaciones")

class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha de fin")
    objetos = models.CharField(max_length=100, verbose_name="Objetos")
    autorizacion = models.BooleanField(default=False)
    idVisitante_permi = models.ForeignKey(Visitante, on_delete=models.CASCADE, related_name="visitante_permiso", null=True)
    idNiveles_seguridad = models.ForeignKey(Niveles_seguridad, on_delete=models.CASCADE, null=True) 

class Punto_control(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=True)
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion", null=True)


class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, null=True)
    idPtoCrontrol = models.ForeignKey(Punto_control, on_delete=models.CASCADE, null=True)
    hora_ingreso = models.TimeField(verbose_name="Hora de ingreso", null=True)
    hora_salida = models.TimeField(verbose_name="Hora de salida", null=True)

class Punto_control_permiso(models.Model):
    idPunto_control = models.ForeignKey(Punto_control, on_delete=models.CASCADE)
    idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE,null=True)

class Punto_control_Dispositivos(models.Model):
    idPunto_control_dispo = models.ForeignKey(Punto_control, on_delete=models.CASCADE)
    idDispositivos = models.ForeignKey(Dispositivos, on_delete=models.CASCADE)

