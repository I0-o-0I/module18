from django.shortcuts import render
from django.views.generic import TemplateView

def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    list = ['Игра1', 'Игра2', 'Игра3']
    context = {
        'list': list,
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')