from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def usuarios(request):
    return render(request, 'usuarios.html')
