from unicodedata import name
from django.urls import path
from . import views
from django.contrib import admin

import mainSistema.views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('visitante/', mainSistema.views.visitante, name='visitante'),

    path('listado_ingresos/', mainSistema.views.ingreso, name='listado_ingresos'),

    path('ingreso_listado/', mainSistema.views.listado_ingresos, name='listado_ingresos'),

    path('dispositivos/', mainSistema.views.dispositivos, name='dispositivos'),

    path('puntos_de_control/', mainSistema.views.puntos_de_control, name='puntos_de_control'),

    path('permiso/<int:id>', views.permiso, name='permiso'),

    path('reporte_permiso/', views.reporte_permiso, name='reporte_permiso'),

    path('reporte_pts_control/', views.reporte_pts_control, name='reporte_pts_control'),


    path('reporte_visitante/', views.reporte_visitante, name='reporte_visitante'),

    path('generar_QR/', views.generar_QR, name='generar_QR'),

    path('save/', views.save_visitante, name="save"),

    path('prueba/', mainSistema.views.prueba, name='prueba'),

    path('niveles_seguridad/', mainSistema.views.niveles_seguridad, name='niveles_seguridad'),

    path('crear_nivel_seguridad', views.crear_nivel_seguridad, name='crear_nivel_seguridad'),

    path('administrar_niveles', views.administrar_niveles, name='administrar_niveles'),

    path('saveNS/', views.save_niveles_seguridad, name="saveNS"),

    path('saveP/', views.save_permiso, name="saveP"),

    path('saveD/', views.save_dispositivos, name="saveD"),

    path('savePC/', views.save_puntos_de_control, name="savePC"),

    path('editar/', views.editar, name='editar'),

    path('visualizarVisitante',views.visualizarVisitante , name='visualizarVisitante'),

    path('inf_visitante', views.inf_visitante, name="inf_visitante"),

    path('reporte_dispositivos/', views.reporte_dispositivos, name='reporte_dispositivos')
   


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
