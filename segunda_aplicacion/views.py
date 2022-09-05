from django.shortcuts import render

# Create your views here.
def listarDirectores(request):
    datos = {
        "autor": "Djanguito",
        "directores": [
            {"nombre": "Quentin Tarantino", "imagen": "img/quentin.png", "retirado": True},
            {"nombre": "James Gunn", "imagen": "img/james.png", "retirado": False}
        ]
    }
    return render(request, 'segunda_aplicacion/listar_directores.html', datos)

def listarActores(request):
    return render(request, 'segunda_aplicacion/lista_actores.html')