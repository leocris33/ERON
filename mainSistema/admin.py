from django.contrib import admin
from .models import Visitante
from .models import Ingreso
from .models import Niveles_seguridad
from .models import Dispositivos
from .models import Permiso
from .models import Punto_control
from .models import Punto_control_permiso
from .models import Punto_control_Dispositivos

# Register your models here.
admin.site.register(Visitante)
admin.site.register(Ingreso)
admin.site.register(Niveles_seguridad)
admin.site.register(Dispositivos)
admin.site.register(Permiso)
admin.site.register(Punto_control)
admin.site.register(Punto_control_permiso)
admin.site.register(Punto_control_Dispositivos)
