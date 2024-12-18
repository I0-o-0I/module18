from django.shortcuts import render
from django.views.generic import TemplateView

def platform(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    #text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': 'Корзина',
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    title = 'Игры'
    text1 = 'Игра1'
    text2 = 'Игра2'
    text3 = 'Игра3'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'button': 'Купить',
        'button2': 'Назад',
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    title = 'Корзина'
    text1 = 'Корзина пустая'
    context = {
        'title': title,
        'text1': text1,
        'button2': 'Назад',
    }
    return render(request, 'third_task/cart.html', context)


