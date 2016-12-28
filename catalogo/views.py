from django.shortcuts import render
from catalogo.models import Estado, Institucion, Facultad

# Create your views here.

def mandadatos(request):
    datos = Facultad.objects.all() #.order_by('entidad')
    entidad = Estado.objects.all() #.order_by('nombre_estado')
    escuelas = Institucion.objects.all()# .order_by('nombre_estado')

    return  render(request, 'carga_listado.html', {'entidad':entidad, 'escuelas':escuelas, 'datos':datos})