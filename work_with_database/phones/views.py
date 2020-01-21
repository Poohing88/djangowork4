from operator import itemgetter

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    info = []
    if sort == 'name':
        information = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        information = Phone.objects.all().order_by('price')
    else:
        information = Phone.objects.all()
    for i in information:
        read_dick = {'Название': i.name, 'Изображение': i.image, 'Цена': i.price,
                     'Дата_выхода': i.release_date, 'Технология_lte': i.lte_exists, 'slug': i.slug}
        info.append(read_dick)
    context = {'info': info}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    information = Phone.objects.all().filter(slug=slug)
    info = {}
    for i in information:
        read_dick = {'Название': i.name, 'Изображение': i.image, 'Цена': i.price,
                     'Дата_выхода': i.release_date, 'Технология_lte': i.lte_exists, 'slug': i.slug}
        info = read_dick
    context = {"info": info}
    return render(request, template, context)

