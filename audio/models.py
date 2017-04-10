from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

class Testadd(models.Model):
    address = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __unicode__(self):
        return self.address