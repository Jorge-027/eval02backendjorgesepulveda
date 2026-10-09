from django.test import TestCase
from django.urls import reverse

from .views import GENEROS


class PruebasCatalogoPeliculas(TestCase):
	def test_portada_muestra_todos_los_generos(self):
		respuesta = self.client.get(reverse('jorgesepulveda:inicio'))

		self.assertEqual(respuesta.status_code, 200)
		for genero in GENEROS:
			self.assertContains(respuesta, genero['nombre'])

	def test_incluye_todas_las_peliculas_solicitadas(self):
		nombres = {
			nombre
			for genero in GENEROS
			for nombre, anio in genero['peliculas']
		}
		peliculas_solicitadas = {
			'Volver al futuro 2',
			'La Cosa', 'Submarine', 'Scream', 'Django: Unchained',
			'The Darjeeling Limited', 'Euroviaje', 'Saw II', 'Evil Dead II',
			'Hombre lobo americano en Londres',
		}

		self.assertTrue(peliculas_solicitadas.issubset(nombres))

	def test_cada_genero_muestra_al_menos_diez_peliculas(self):
		for genero in GENEROS:
			with self.subTest(genero=genero['identificador']):
				respuesta = self.client.get(
					reverse('jorgesepulveda:detalle_genero', args=[genero['identificador']])
				)

				self.assertEqual(respuesta.status_code, 200)
				self.assertGreaterEqual(respuesta.content.count(b'class="card movie-card'), 10)
				self.assertEqual(respuesta.content.count(b'images/peliculas/'), 10)
				self.assertNotContains(respuesta, 'images.unsplash.com')
				self.assertContains(respuesta, 'alt="Imagen de')

	def test_genero_desconocido_devuelve_no_encontrado(self):
		respuesta = self.client.get(
			reverse('jorgesepulveda:detalle_genero', args=['genero-inexistente'])
		)

		self.assertEqual(respuesta.status_code, 404)
