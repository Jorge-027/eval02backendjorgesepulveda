from django.http import Http404
from django.shortcuts import render

GENEROS = [
    {
        'identificador': 'drama',
        'nombre': 'Drama',
        'descripcion': 'Para hacerte llorar o enojar o ambos'
        'acento': 'terracota',
        'peliculas': [
            ('Sueños de libertad', 1994), ('Django Unchained', 2012),
            ('Forrest gump', 1994), ('Submarine', 2010),
            ('La vida es bella', 1997), ('12 años de esclavitud', 2013),
            ('El club de los poetas muertos', 1989), ('Una mente brillante', 2001),
            ('Historia de un matrimonio', 2019), ('Parasitos', 2019),
        ],      
    },
    {
        'identificador': 'ciencia ficcion',
        'nombre': 'Ciencia ficción',
        'descripcion': 'Todo fantasioso para olvidar lo aburrido de lo convencional',
        'acento': 'lime',
        'peliculas': [
            ('2001: Odisea del espacio', 1968), ('Blade Runner', 1982),
            ('Volver al futuro 2', 1989), ('Matrix', 1999),
            ('Interestellar', 2014), ('la llegada', 2016),
            ('Duna', 2021), ('Ex Machina', 2014),
            ('E.T el extraterrestre', 1982), ('hijos de los hombres', 2006),
        ],

    },
    {
        'identificador': 'comedia',
        'nombre': 'Comedia',
        'descripcion': 'Para hacerte reir y pasar los malos ratos',
        'acento': 'yellow',
        'peliculas': [
            ('tiempos moderos', 1936), ('Una eva y dos adanes', 1933),
            ('the darjleeling limited', 2007), ('euroviaje', 2004),
            ('el dia de la marmota', 1993), ('¿Quieres ser John Malkovich?', 1993),
            ('Little Miss Sunshine', 2006), ('¿Que paso ayer?', 2009),
            ('JoJo Rabbit', 2019), ('palm springs', 2020),
        ],
    },
    {
        'identificador': 'terror',
        'nombre': 'Terror',
        'descripcion': 'Miedo o no miedo',
        'acento': 'terracota',
        'peliculas': [ 
            	('La Cosa', 1982), ('Scream', 1996),
			('Saw II', 2005), ('Evil Dead II', 1987),
			('Hombre lobo americano en Londres', 1981),
			('El exorcista', 1973), ('El resplandor', 1980),
			('Pesadilla en la calle Elm', 1984),
			('La noche de los muertos vivientes', 1968),
			('Hereditary', 2018),
		],
	},
]

IMAGENES_PELICULAS = {
	'2001: Odisea del espacio': 'images/peliculas/ciencia-ficcion/2001unaodisea.jpg',
	'Blade Runner': 'images/peliculas/ciencia-ficcion/bladerunner.jpg',
	'Volver al futuro 2': 'images/peliculas/ciencia-ficcion/volveralfuturo2.jpg',
	'Matrix': 'images/peliculas/ciencia-ficcion/matrix.jpg',
	'Interestelar': 'images/peliculas/ciencia-ficcion/interestelar.jpg',
	'La llegada': 'images/peliculas/ciencia-ficcion/lallegada.jpg',
	'Duna': 'images/peliculas/ciencia-ficcion/duna.jpg',
	'Ex Machina': 'images/peliculas/ciencia-ficcion/exmachina.jpg',
	'E.T., el extraterrestre': 'images/peliculas/ciencia-ficcion/et.jpg',
	'Hijos de los hombres': 'images/peliculas/ciencia-ficcion/hijos-de-los-hombres.jpg',
	'Tiempos modernos': 'images/peliculas/comedia/tiemposmodernos.jpg',
	'Una Eva y dos Adanes': 'images/peliculas/comedia/unaevaydosadanes.jpg',
	'The Darjeeling Limited': 'images/peliculas/comedia/darjeeling.jpg',
	'Euroviaje': 'images/peliculas/comedia/euroviaje.jpg',
	'El día de la marmota': 'images/peliculas/comedia/diadelamarmota.jpg',
	'¿Quieres ser John Malkovich?': 'images/peliculas/comedia/quieres-ser-john-malkovich.jpg',
	'Little Miss Sunshine': 'images/peliculas/comedia/little-miss-sunshine.jpg',
	'¿Qué pasó ayer?': 'images/peliculas/comedia/quepasoayer.jpg',
	'Jojo Rabbit': 'images/peliculas/comedia/jojorabbit.jpg',
	'Palm Springs': 'images/peliculas/comedia/palmsprings.jpg',
	'Sueños de libertad': 'images/peliculas/drama/suenos-de-libertad.jpg',
	'Django: Unchained': 'images/peliculas/drama/djangounchained.jpg',
	'Forrest Gump': 'images/peliculas/drama/forrestgump.jpg',
	'Submarine': 'images/peliculas/drama/submarine.jpg',
	'La vida es bella': 'images/peliculas/drama/lavidaesbella.png',
	'12 años de esclavitud': 'images/peliculas/drama/12-anos-de-esclavitud.jpg',
	'El club de los poetas muertos': 'images/peliculas/drama/club-de-los-poetas-muertos.jpg',
	'Una mente brillante': 'images/peliculas/drama/unamentebrillante.jpg',
	'Historia de un matrimonio': 'images/peliculas/drama/historia-de-un-matrimonio.jpg',
	'Parásitos': 'images/peliculas/drama/parasitos.jpg',
	'La Cosa': 'images/peliculas/terror/la cosa.jpg',
	'Scream': 'images/peliculas/terror/scream.jpg',
	'Saw II': 'images/peliculas/terror/saw2.jpg',
	'Evil Dead II': 'images/peliculas/terror/evil-dead-ii.jpg',
	'Hombre lobo americano en Londres': 'images/peliculas/terror/hombreloboamericano.jpg',
	'El exorcista': 'images/peliculas/terror/elexorcista.jpg',
	'El resplandor': 'images/peliculas/terror/elresplandor.jpg',
	'Pesadilla en la calle Elm': 'images/peliculas/terror/pesadillaenlacalleelm.jpg',
	'La noche de los muertos vivientes': 'images/peliculas/terror/lanochedelosmuertosvivientes.jpg',
	'Hereditary': 'images/peliculas/terror/hereditary.jpg',
}

def inicio(solicitud):
	return render(solicitud, 'jorgesepulveda/index.html', {'generos': GENEROS})

def detalle_genero(solicitud, genero_slug):
	genero = next(
		(genero_encontrado for genero_encontrado in GENEROS if genero_encontrado['identificador'] == genero_slug),
		None,
	)
	if genero is None:
		raise Http404('Género no encontrado')

	peliculas = [
		{
			'nombre': nombre,
			'año': año,
			'imagen': URLS_IMAGENES[indice % len(URLS_IMAGENES)],
		}
		for indice, (nombre, año) in enumerate(genero['peliculas'])
	]
	return render(
		solicitud,
		'jorgesepulveda/genre_detail.html',
		{'genero': genero, 'peliculas': peliculas},
	)
