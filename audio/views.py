#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(r):
	return HttpResponse('Welcome')

def cal_get(r):
	a = r.GET.get('a', 0)
	b = r.GET.get('b', 0)
	c = int(a) + int(b)
	return HttpResponse('%s + %s = %s' %(a, b, c))

def cal_post(r,a,b):
	c = int(a) + int(b)
	return HttpResponse('%s + %s = %s' %(a, b, c))

def test_template(r):
	return render(r, 'test_template.html', {'username':'zhang'})


