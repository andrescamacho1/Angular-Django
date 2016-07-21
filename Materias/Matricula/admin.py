from django.contrib import admin
from .models import Alumno
from .models import Materia
# Register your models here.


class D_Materia(admin.ModelAdmin):
	list_display=["__str__","nombre"]
	class Meta:
		model=Materia
admin.site.register(Materia,D_Materia)


class D_Alumno(admin.ModelAdmin):
	list_display=["__str__","cedula","nombre","apellido","edad","genero","email","telefono"]
	class Meta:
		model=Alumno
admin.site.register(Alumno,D_Alumno)
