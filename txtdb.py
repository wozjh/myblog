#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import os
# os.environ.setdefault('DJANGO_SETTINGS_MOUDLE', 'myblog.settings')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
import django
if django.VERSION >= (1.7):
    django.setup()

def main():
    from audio.models import Person
    with open('oldblog.txt') as f:
        PersonList = []
        for line in f:
            name, age = line.split('****')
            PersonList.append(Person(name=name, age=age))

    Person.objects.bulk_create(PersonList)

if __name__ == "__main__":
    main()
    print ('Done')
