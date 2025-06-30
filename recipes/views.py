from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name': 'Luan Souza',
    })


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return render(request, 'recipes/contato.html')
