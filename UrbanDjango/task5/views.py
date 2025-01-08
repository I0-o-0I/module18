from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

list_user = ['Tom', 'Bob', 'Tim']

def sign_up_by_html(request):
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse('Вы должны быть старше 18')
        elif username in list_user:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')
        else:
            list_user.append(username)
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
            elif username in list_user:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            else:
                list_user.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)

