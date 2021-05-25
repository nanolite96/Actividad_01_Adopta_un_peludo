from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "inicio.html")

def perros(request):
    return render(request, "perros.html")

def gatos(request):
    return render(request, "gatos.html")

def contacto(request):
    return render(request, "contactar.html")

def ubicacion(request):
    return render(request, "ubicacion.html")

def gracias(request):
    return render(request, "gracias.html")

def gracias2(request):
    return render(request, "gracias2.html")

def loki(request):
    return render(request, "loki.html")

def princesa(request):
    return render(request, "princesa.html")

def timmy(request):
    return render(request, "timmy.html")

def adoptar(request):
    return render(request, "adoptar.html")

def bigotes(request):
    return render(request, "bigotes.html")

def manchita(request):
    return render(request, "manchita.html")

def sara(request):
    return render(request, "sara.html")