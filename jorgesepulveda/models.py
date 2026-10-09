from django.db import models

class genero(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    genero = models.ForeignKey(
        genero,
        on_delete=models.CASCADE,
        related_name='peliculas'
    )
    titulo = models.CharField(max_length=200)
    Año_de_estreno = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['titulo']
        constraints = [
            models.uniqueconstraint(
                fields=['genero', 'titulo'],
                name='unique_genero_titulo'
            )
        ]

    def __str__(self):
        return f"{self.titulo} ({self.Año_de_estreno})"