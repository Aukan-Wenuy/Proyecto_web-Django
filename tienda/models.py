from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'
        
    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True, null=True, upload_to='tienda/')
    precio=models.FloatField()    
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        

    def __str__ (self):
        return ' El nombre es : %s | La Categoria es : %s |  El precio es : %s ' % (self.nombre, self.categorias, self.precio)
    
