from Matricula.models import Materia,Alumno
from rest_framework import serializers

class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumno
		fields=['idCA','cedula','nombre','apellido']

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=['nombre','cupos']