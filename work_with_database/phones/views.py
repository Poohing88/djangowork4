from operator import itemgetter

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    information = Phone.objects.all()
    info = []
    for i in information:
        read_dick = {'Название': i.name, 'Изображение': i.image, 'Цена': i.price,
                     'Дата_выхода': i.release_date, 'Технология_lte': i.lte_exists, 'slug': i.slug}
        info.append(read_dick)
    if sort == 'name':
        info.sort(key=itemgetter('Название'))
    elif sort == 'min_price':
        info.sort(key=itemgetter('Цена'))
    else:
        info = info
    context = {'info': info}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    information = Phone.objects.all()
    info = {}
    for i in information:
        read_dick = {'Название': i.name, 'Изображение': i.image, 'Цена': i.price,
                     'Дата_выхода': i.release_date, 'Технология_lte': i.lte_exists, 'slug': i.slug}
        if read_dick['slug'] == slug:
            info = read_dick
    context = {"info": info}
    return render(request, template, context)

