from django.db import models

# Create your models here.
class Category(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.nombre)

class Articulo(models.Model):
    id_articulo= models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0)
    marca = models.CharField(max_length=50, blank=True, null=True)
    count_in_stock = models.IntegerField(null=True, blank=True, default=0)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.nombre)

