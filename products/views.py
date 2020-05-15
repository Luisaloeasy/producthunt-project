from django.shortcuts import render

#Creo la funcion home que esta siendo llamada por urls.py
#Luego de crear la funcion debo crear templates/nameapp/home.html

def home(request):
    return render(request, 'products/home.html')
