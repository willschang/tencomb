# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    context = {'home': '欢迎您来到10.com！'}
    return render(request, 'home.html', context)