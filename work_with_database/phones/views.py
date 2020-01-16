from django.shortcuts import render
from phones.read_csv import read_csv

info = read_csv()


def show_catalog(request):
    template = 'catalog.html'
    context = {'info': info}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
