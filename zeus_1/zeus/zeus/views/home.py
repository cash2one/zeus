# -*- coding: utf-8 -*-

from django.shortcuts import render
from zeus.models import Item

def index(request):
    item = Item.objects.order_by('id')[0]
    context = {'myname': item.label}
    return render(request, 'index.html', context)
