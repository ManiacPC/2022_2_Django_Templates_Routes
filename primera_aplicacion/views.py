from django.shortcuts import render

# Create your views here.
def listarPeliculas(request):
    return render(request, 'primera_aplicacion/listar_peliculas.html')
