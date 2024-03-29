from django.shortcuts import render


def home(request):
    # Variables que se van a mandar al template mediante el contexto
    nombre = 'Nelson'
    apellido = 'Figueroa'
    owner_name = {
        # diccionario de contexto
        # clave que usa la template : valor que queramos darle.
        'name' : nombre,
        'lastname' : apellido
    }
    return render(request, 'core/home.html', context=owner_name)

def about(request):
	return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')