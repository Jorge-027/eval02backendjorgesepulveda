from django.urls import path

from . import views

app_name = 'jorgesepulveda'

urlpatterns = [
    path('', views.inicio, name='index'),
    path('generos/<slug:genero_slug>/', views.detalle_genero, name='detalle_genero'),
    ]