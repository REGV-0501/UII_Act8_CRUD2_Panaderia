from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

# Listar empleados
def index(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

# Ver empleado
def ver_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'ver_empleado.html', {'empleado': empleado})

# Agregar empleado
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        edad = request.POST['edad']
        correo = request.POST['correo']
        numero_telefono = request.POST['numero_telefono']
        Empleado.objects.create(nombre=nombre, apellidos=apellidos, edad=edad, correo=correo, numero_telefono=numero_telefono)
        return redirect('inicio')
    return render(request, 'agregar_empleado.html')

# Editar empleado
def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellidos = request.POST['apellidos']
        empleado.edad = request.POST['edad']
        empleado.correo = request.POST['correo']
        empleado.numero_telefono = request.POST['numero_telefono']
        empleado.save()
        return redirect('inicio')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

# Borrar empleado
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})