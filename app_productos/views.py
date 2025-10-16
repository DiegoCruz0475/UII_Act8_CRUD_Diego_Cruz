from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Listar estudiantes
def index(request):
    productos = Producto.objects.all()
    return render(request, 'verproductos.html', {'productos': productos})

# Ver estudiante (opcional, puedes usarlo si quieres detalle)
def listaproductos(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'verproductos.html', {'productos': producto})

# Agregar estudiante
def agregarproducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        material = request.POST['material']
        peso = request.POST['peso']
        stock = request.POST['stock']
        Producto.objects.create(nombre=nombre, tipo=tipo, material=material, peso=peso, stock=stock)
        return redirect('index')
    return render(request, 'agregarproducto.html')

# Editar estudiante
def editarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.tipo = request.POST['tipo']
        producto.material = request.POST['material']
        producto.peso = request.POST['peso']
        producto.stock = request.POST['stock']       
        producto.save()
        return redirect('index')
    return render(request, 'editarproducto.html', {'producto': producto})

# Borrar estudiante
def borrarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return render(request, 'borrarproducto.html', {'producto': producto})