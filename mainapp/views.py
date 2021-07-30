from django.shortcuts import render
from mainapp.models import Product


def index(request):
    links_menu = [
        {'href': 'index', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    products = Product.objects.all()[:4]

    context = {
        'title': "Магазин",
        'links_menu': links_menu,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context)
