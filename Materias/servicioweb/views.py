from Matricula.models  import Alumno,Materia
from rest_framework import viewsets
from .serializable import AlumnoSerializable,MateriaSerializable

class AlumnoViewSet(viewsets.ModelViewSet):
	queryset=Alumno.objects.all().order_by("nombre")
	serializer_class=AlumnoSerializable

class MateriaViewSet(viewsets.ModelViewSet):
	queryset=Materia.objects.filter(cupos__lte=29)
	serializer_class=MateriaSerializable


# Create your views here.
