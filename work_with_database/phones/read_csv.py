import csv
from datetime import datetime

from django.template.defaultfilters import slugify


def read_csv():
    with open('phones.csv', mode='r') as csvfile:
        phone_reader = csv.reader(csvfile, delimiter=';')
        # пропускаем заголовок
        next(phone_reader)
        phones_viev = []
        for line in phone_reader:
            name = line[1]
            image = line[2]
            price = int(line[3])
            date = line[4].replace('-', '')
            date = datetime.strptime(date, '%Y%m%d')
            lte = line[5]
            slug = slugify(name)
            info = {'Название': name, 'Изображение': image, 'Цена': price,
                    'Дата_выхода': date, 'Технология_lte': lte, 'slug': slug}
            phones_viev.append(info)
        return phones_viev
