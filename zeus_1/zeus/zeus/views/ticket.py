# -*- coding: utf-8 -*-

import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from zeus.models import Ticket

def index(request):
    tickets = []
    for ticket in Ticket.objects.order_by('create_time'):
        tickets.append({
            'id': ticket.id,
            'type': ticket.get_type_id_display(),
            'create_time': ticket.create_time.strftime('%Y-%m-%d %H:%M:%S')
        })
    return render(request, 'ticket/index.html', {'tickets': tickets})

def add(request):

    if request.method == 'POST':
        type_id = int(request.POST['type_id'])
        ticket = Ticket()
        ticket.type_id = type_id
        ticket.detail = json.dumps(make_detail(request, type_id))
        ticket.create_time = datetime.datetime.now()
        ticket.save()
        return redirect('/ticket/')

    return render(request, 'ticket/add.html', {'ticket_types': Ticket.TYPES})

def edit(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        type_id = int(request.POST['type_id'])
        ticket.type_id = type_id
        ticket.detail = json.dumps(make_detail(request, type_id))
        ticket.save()
        return redirect('/ticket/')

    detail = json.loads(ticket.detail)
    context = {
        'ticket_types': Ticket.TYPES,
        'id': ticket.id,
        'type_id': ticket.type_id,
        'os': detail.get('os', ''),
        'hd': detail.get('hd', '')
    }

    return render(request, 'ticket/add.html', context)

def make_detail(request, type_id):

    if type_id == 1: # 重装系统
        detail = {
            'os': request.POST['os']
        }

    elif type_id == 2: # 配件升级
        detail = {
            'hd': request.POST['hd']
        }

    else:
        raise ValueError

    return detail
