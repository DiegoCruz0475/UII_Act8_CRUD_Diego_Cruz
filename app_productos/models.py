from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    peso=models.DecimalField(max_digits=5, decimal_places=2)
    stock=models.PositiveIntegerField()

    def __str__(self):
        return f'Producto: {self.nombre} {self.tipo} {self.material} {self.peso} {self.stock}'