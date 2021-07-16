from django.shortcuts import render


def index(request):
    return render(request, 'GeekShop/index.html')


def contacts(request):
    return render(request, 'GeekShop/contact.html')
