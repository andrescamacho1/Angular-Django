from django.db import models

# Create your models here.

class Materia(models.Model):
	nombre=models.CharField(max_length=20)
	cupos=models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	
	list_genero=(
		('Masculino','Masculino'),
		('Femenino','Femenino'),
	)
	idCA = models.ForeignKey(Materia, on_delete=models.CASCADE,default="")
	cedula=models.CharField(max_length=12,default="",unique=True)
	nombre=models.CharField(max_length=25)
	apellido=models.CharField(max_length=30)
	edad=models.SmallIntegerField(default=0)
	email=models.EmailField(max_length=30,blank=True,null=True)
	telefono=models.CharField(max_length=10,blank=True,null=True)
	genero=models.CharField(max_length=10,choices=list_genero,default="Masculino")

	def __str__(self):
		return self.cedula