import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                name = line[1]
                image = line[2]
                price = int(line[3])
                date = line[4].replace('-', '')
                date = datetime.strptime(date, '%Y%m%d')
                lte = line[5]
                slug = slugify(name)
                phones = Phone(name=name, image=image, price=price, release_date=date, lte_exists=lte, slug=slug)
                phones.save()


