from django.urls import path
from. import views


urlpatterns = [
    # Otras rutas aquí...
  
    path('inicio/', views.inicio, name='inicio'),
    path('insertar_usuario/', views.insertar_usuario, name='insertar_usuario'),
    path('mostrar_usuario/', views.mostrar_usuario, name='mostrar_usuario'),
    path('login/', views.login, name='login'),
    path('insertar_juego/', views.insertar_juego, name='insertar_juego'),
    path('mostrar_juego/', views.mostrar_juego, name='mostrar_juego'),
    path('insertar_pelicula/', views.insertar_pelicula, name='insertar_pelicula'),
    path('mostrar_peliculas/', views.mostrar_peliculas, name='mostrar_peliculas'),
    path('insertar_capitulo/', views.insertar_capitulo, name='insertar_capitulo'),
    path('mostrar_capitulo/', views.mostrar_capitulo, name='mostrar_capitulo'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('calculadora_para_invitados/', views.calculadora_para_invitados, name='calculadora_para_invitados'),
    path('salva_juego/', views.salva_juego, name='salva_juego'),
    path('fijando_archivo_para_descragar/', views.fijando_archivo_para_descragar, name='fijando_archivo_para_descragar'),
    path('descargar_archivo/', views.descargar_archivo, name='descargar_archivo'),
    path('salva_juego_usuarios/', views.salva_juego_usuarios, name='salva_juego_usuarios'),













 



]