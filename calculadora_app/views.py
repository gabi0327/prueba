# Create your views here.
from django.shortcuts import render




def salva_juego(request):
    return render(request,'salva_juego.html')

def calculadora_para_invitados(request):
    return render(request,'calculadora_para_invitados.html')


def calculadora(request):
    return render(request,'calculadora.html')



def mostrar_capitulo(request):
    return render(request,'mostrar_capitulo.html')


def insertar_capitulo(request):
    return render(request,'insertar_capitulo.html')




def mostrar_peliculas(request):
    return render(request,'mostrar_pelicula.html')


def insertar_pelicula(request):
    return render(request,'insertar_pelicula.html')





def mostrar_juego(request):
    return render(request,'mostrar_juego.html')


def insertar_juego(request):
    return render(request,'insertar_juego.html')




def login(request):
    return render(request,'login.html')



def mostrar_usuario(request):
    return render(request,'mostrar_usuario.html')


def insertar_usuario(request):
    return render(request,'insertar_usuario.html')


def inicio(request):
    return render(request,'inicio.html')


