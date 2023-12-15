from django import views
from django.urls import path

import Aplicaciones.Academico.views

urlpatterns =[
    path('', Aplicaciones.Academico.views.home),
    path('registrarCurso/', Aplicaciones.Academico.views.registrarCurso),
    path('edicionCurso/<codigo>', Aplicaciones.Academico.views.edicionCurso),
    path('editarCurso/', Aplicaciones.Academico.views.editarCurso),
    path('eliminarCurso/<codigo>', Aplicaciones.Academico.views.eliminarCurso)
]