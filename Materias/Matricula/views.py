from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Materia,Alumno
from .forms import Form_Alumnos,Form_Materia


def inicio(request):
	return render(request,"inicio.html",{})

def listar(request):
	alumno=Alumno.objects.all()
	materia=Materia.objects.all()
	context={'alumno':alumno,
			 'materia':materia}
	return render(request,"listarAlumno.html",context)

def crearMateria(request):
	form=Form_Materia(request.POST or None)
	context={'f':form,}
	if request.method=='POST':
		if form.is_valid():
			lector=form.cleaned_data
			i=lector.get("nombre")
			c=lector.get("cupos")		
			obj=Materia.objects.create(nombre=i,cupos=c)
			if obj:
				return redirect(listar)
	return render(request,"crearMateria.html",context)


def crear(request):
	form=Form_Alumnos(request.POST or None)
	context={'f':form,}
	if request.method=='POST':
		if form.is_valid():
			lector=form.cleaned_data
			i=lector.get("idCA")
			c=lector.get("cedula")
			n=lector.get("nombre")
			a=lector.get("apellido")
			e=lector.get("edad")
			em=lector.get("email")
			g=lector.get("genero")
			t=lector.get("telefono")
			obj=Alumno.objects.create(idCA=i,cedula=c,nombre=n,apellido=a,edad=e,email=em,telefono=t)
			if obj:
				return redirect(listar)
	return render(request,"crear.html",context)

def modificar(request):
	f=Form_Alumnos(request.POST or None)
	usuario=Alumno.objects.get(cedula=request.GET['cedula'])
	context={
		'form':f,
		'usuario':usuario,
	
	}
	f.fields['cedula'].initial=usuario.cedula
	f.fields['nombre'].initial=usuario.nombre
	f.fields['apellido'].initial=usuario.apellido
	f.fields['edad'].initial=usuario.edad
	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			usuario.nombre=datos.get('nombre')
			usuario.apellido=datos.get('apellido')
			usuario.edad=datos.get('edad')
			if(usuario.save()):
				messages.add_message(request,messages.ERROR,"No se a podido guardar los cambios",fail_silently=True)
			else:
				messages.add_message(request,messages.SUCCESS,"Cambios guardados con exito", fail_silently=True)
			return redirect(listar)
	return render(request,"modificar.html",context)


def modificarMaterias(request):
	f=Form_Materia(request.POST or None)
	usuario=Materia.objects.get(nombre=request.GET['nombre'])
	context={
		'form':f,
		'usuario':usuario,
	}
	f.fields['nombre'].initial=usuario.nombre
	f.fields['cupos'].initial=usuario.cupos
	if request.method=='POST':
		if f.is_valid():
			datos=f.cleaned_data
			usuario.nombre=datos.get('nombre')
			usuario.cupos=datos.get('cupos')
			if(usuario.save()):
				messages.add_message(request,messages.ERROR,"No se a podido guardar los cambios",fail_silently=True)
			else:
				messages.add_message(request,messages.SUCCESS,"Cambios guardados con exito", fail_silently=True)
			return redirect(listar)
	return render(request,"modificarMaterias.html",context)


def eliminar(request):
	usuario=Alumno.objects.get(cedula=request.GET['cedula'])
	if usuario.delete():
		messages.add_message(request, messages.SUCCESS, "Se a eliminado con exito a este usuario", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se a logrado eliminar e este al usuario", fail_silently=True)
	return redirect(listar)

def transaccion(request):
	usuario=Cliente.objects.all(cedula=request.GET['cedula'])


def eliminarMateria(request):
	usuario=Materia.objects.get(nombre=request.GET['nombre'])
	if usuario.delete():
		messages.add_message(request, messages.SUCCESS, "Se a eliminado con exito a esta materia", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se a logrado eliminar esta materia", fail_silently=True)
	return redirect(listar)


