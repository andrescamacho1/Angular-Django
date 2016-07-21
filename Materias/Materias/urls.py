"""Materias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from servicioweb.views import AlumnoViewSet,MateriaViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'Alumno',AlumnoViewSet)
router.register(r'Materia',MateriaViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^$','caja.views.inicio',name='root'),
    url(r'^listar/$','Matricula.views.listar',name='listarAlumno'),
    #url(r'^listarAlumno/$','Matricula.views.listarAlumno',name='listarAlumno'),
    url(r'^crear/$','Matricula.views.crear',name='crear'),
    url(r'^crearMateria/$','Matricula.views.crearMateria',name='crearMateria'),
    url(r'^modificar/$','Matricula.views.modificar',name='modificar'),
    url(r'^modificarMaterias/$','Matricula.views.modificarMaterias',name='modificarMaterias '),
    url(r'^eliminar/$', 'Matricula.views.eliminar',name='eliminar'),
    url(r'^eliminarMateria/$', 'Matricula.views.eliminarMateria',name='eliminarMateria'),
    url(r'^',include(router.urls)),
 
]
