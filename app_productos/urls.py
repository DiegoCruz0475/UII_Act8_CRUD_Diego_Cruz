from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>', views.listaproductos, name='listaproductos'),
    path('agregar/', views.agregarproducto, name='agregarproducto'),
    path('editar/<int:id>/', views.editarproducto, name='editarproducto'),
    path('borrar/<int:id>/', views.borrarproducto, name='borrarproducto')
]