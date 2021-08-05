from django.shortcuts import render
from mainapp.views import get_basket


def index(request):
    context = {
        'slogan': "СУПЕР ПРЕДЛОЖЕНИЕ",
        'basket': get_basket(request.user),
        'title': "Главная"
    }
    return render(request, 'GeekShop/index.html', context)


def contacts(request):
    title = "Контакты"

    context = {
        'basket': get_basket(request.user),
        'title': title,
    }
    return render(request, 'GeekShop/contact.html', context)
