from operator import itemgetter

from django.shortcuts import render
from phones.read_csv import read_csv




def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    info = read_csv()
    if sort == 'name':
        info = info.sort(key=itemgetter('Название'))
    elif sort == 'min_price':
        info = info.sort(key=itemgetter('Цена'))
    else:
        info = info
    context = {'info': info}
    return render(request, template, context)


def show_product(request, slug):
    template = f'{slug}.html'
    info = read_csv()
    telefon = str()
    for i in info:
        if i['slug'] == slug:
            telefon = i
        else:
            telefon = None
    context = {"info": telefon}
    return render(request, template, context)
