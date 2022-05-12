from unicodedata import name
from django.urls import path
from . import views
from django.contrib import admin

import mainSistema.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('visitante/', mainSistema.views.visitante, name='visitante'),
    path('ingreso/', mainSistema.views.ingreso, name='ingreso'),
    path('dispositivos/', mainSistema.views.dispositivos, name='dispositivos'),
    path('puntos_de_control/', mainSistema.views.puntos_de_control, name='puntos_de_control'),
    path('permiso/', views.permiso, name='permiso'),
    path('reporte_visitante/', views.reporte_visitante, name='reporte_visitante'),
    path('generar_QR/', views.generar_QR, name='generar_QR'),
    path('save/', views.save_visitante, name="save"),
    path('pruebas_orm/', views.pruebas_orm, name="pruebas_orm"),
    path('prueba/', mainSistema.views.prueba, name='prueba'),
    path('niveles_seguridad/', mainSistema.views.niveles_seguridad, name='niveles_seguridad'),
    path('crear_nivel_seguridad', views.crear_nivel_seguridad, name='crear_nivel_seguridad'),
    path('administrar_niveles', views.administrar_niveles, name='administrar_niveles'),
    path('saveNS/', views.save_niveles_seguridad, name="saveNS"),
    
    
   
    
    
    


  

  
]  
