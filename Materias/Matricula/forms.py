from django import forms
from .models import Alumno,Materia
class Form_Materia(forms.ModelForm):
	class Meta:
		model=Materia
		fields=["nombre","cupos"]
class Form_Alumnos(forms.ModelForm):
	class Meta:
		model=Alumno
		fields=["idCA","cedula","nombre","apellido","edad","email","genero","telefono"]