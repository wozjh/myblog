#-*- coding: utf-8 -*-
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

class Article(models.Model):
    title = models.CharField(u'标题', max_length=30)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title

