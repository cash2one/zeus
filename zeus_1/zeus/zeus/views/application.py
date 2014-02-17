# -* - coding: utf-8 -*-

from django.shortcuts import render, redirect,render_to_response,HttpResponse

from zeus.models import Ticket
from zeus.models import User
from zeus.models import Process
from zeus.models import Item
from zeus.models import Network
from zeus.models import Rack
from zeus.models import Ticket_status
from zeus.models import Memory
from django.db.models import Q
import re
import json
import datetime
import simplejson

def index(request):
#    if request.method=='GET':
    if request.GET:
        id = request.GET.get('id')
#            return render(request,'https://auth.corp.anjuke.com/login.php?client_id=zeus&client_secret=d2db7537&grant_type=authorization_code&code=e9d3aa24df58412d23eefd5a8143a244')
#        else:
        user=User.objects.get(id=id)
    
        request.session['user']=user
        tickets = Ticket.objects.all().order_by('-id')[:15]
#            return redirect('/index/')

        return render_to_response('home.html', {'user' : user,'tickets' : tickets})
    if request.session['user'] > 0:
        id = request.session['user'].id
        user = User.objects.get(id=id)
        tickets = Ticket.objects.all().order_by('-id')[:15]
        return render_to_response('home.html', {'user' : user,'tickets' : tickets})

#    elif request.method=='':
#        if request.session['user'] > 0:

#    return render_to_response('home.html', {'user' : request.session['user']})
#        return render(request,'https://auth.corp.anjuke.com/login.php?client_id=zeus&client_secret=d2db7537&grant_type=authorization_code&code=e9d3aa24df58412d23eefd5a8143a244')

def page2(request):
    tickets = Ticket.objects.all().order_by('id')[15:30]
    return render_to_response('page2.html', {'user' : request.session['user'],'tickets' : tickets})
def page3(request):
    tickets = Ticket.objects.all().order_by('id')[30:45]
    return render_to_response('page3.html', {'user' : request.session['user'],'tickets' : tickets})
def page4(request):
    tickets = Ticket.objects.all().order_by('id')[45:60]
    return render_to_response('page4.html', {'user' : request.session['user'],'tickets' : tickets})
#def page1(request):
#    items = Item.objects.filter(label='app10-021')
#    item_id = items.id
#    ips = Network.objects.filter(item_id = '22')
#    tickets = Ticket.objects.all().order_by('-id')
#    return render_to_response('page1.html', {'user' : request.session['user'],'tickets' : tickets,'items' : items})

def ajax(request):
    data = {}
    label =  request.POST.get('hostname')
    items = Item.objects.get(label=label)
    item_id = items.id
    networks = Network.objects.get(item_id=item_id,eth="eth0")
    racs = Network.objects.filter(item_id=item_id,eth="rac")   
    rack_id = items.rack_id
    racks = Rack.objects.get(id=rack_id)
    owner_id = items.owner_id
    owner = User.objects.get(id=owner_id)
    data['location'] = racks.name
    data['id'] = items.id
    data['sn'] = items.sn
    data['hd'] = items.hd
    data['mem'] = items.ram
    data['ip'] = networks.ipv4
    data['owner'] = owner.chinese_name
    if len(racs) > 0:
        for rac in racs:
            data['rac'] = rac.ipv4
    else:
        data['rac'] = 'NULL'
    json = simplejson.dumps(data) 
    return HttpResponse(json) 


def application(request):
    if request.method=='POST':
    
        if request.POST['Submit']=='add1':
    
            ticket = Ticket()
            ticket.type_id = '备机申请'
            ticket.hostname_id = request.POST['host']
            ticket.ip_list = request.POST['ip_list']
            ticket.idc_id = request.POST['idc']
            ticket.disk = request.POST['disk']
            ticket.memory = request.POST['mem']
            ticket.os = request.POST['os']
            ticket.comment = request.POST['use']
            ticket.Expectation_time = request.POST['date']
            ticket.raid_id = request.POST['raid']
            ticket.create_time= datetime.datetime.now()
            ticket.user_id = request.session['user'].id
            ticket.detail = request.POST['textarea']
            ticket.ticket_status_id = '1'
            ticket.save()
            return redirect('/index/application')
    
        if request.POST['Submit']=='add2':

            ticket = Ticket()
            ticket.type_id = '服务器报修'
            ticket.ticket_status_id = '1'
            ticket.hostname_id = request.POST['host'] 
            ticket.ip_list = request.POST['ip']
            ticket.idc_id = request.POST['idc']
            ticket.rack_id = request.POST['location1']
            ticket.sn_id = request.POST['sn']
            ticket.variety = request.POST['variety']
            ticket.Expectation_time = request.POST['date']
            ticket.create_time = datetime.datetime.now()
            ticket.host_status = request.POST['host_status'] 
            ticket.user_id = request.session['user'].id
            ticket.detail = request.POST['textarea']
            ticket.save()
            return redirect('/index/application')
              
        if request.POST['Submit'] == 'add3':
         
            ticket = Ticket()
            ticket.type_id = '服务器更换机房'
            ticket.ticket_status_id = '1'
            ticket.hostname_id = request.POST['host']
            ticket.ip_list = request.POST['ip']
            ticket.idc_id = request.POST['old_idc']
            ticket.owner_id = request.POST['old_owner']
            ticket.new_owner = request.POST['now_owner']
            ticket.new_idc = request.POST['now_idc']
            ticket.Expectation_time = request.POST['date']
            ticket.create_time = datetime.datetime.now()
            ticket.user_id = request.session['user'].id
            ticket.os = request.POST['os']
            ticket.detail = request.POST['textarea']
            ticket.save()
            return redirect('/index/application')


        if request.POST['Submit'] == 'add4':

            ticket = Ticket()
            ticket.type_id = '配件升级'
            ticket.ticket_status_id = '1'
            ticket.hostname_id = request.POST['host']
            ticket.ip_list = request.POST['ip']
            ticket.os = request.POST['os']
            ticket.owner_id = request.POST['owner']
            ticket.resource_lists = request.POST['resource']
            ticket.rack_id = request.POST['location1']
            ticket.idc_id = request.POST['idc']
            ticket.Expectation_time = request.POST['date']
            ticket.create_time = datetime.datetime.now()
            ticket.user_id = request.session['user'].id
            ticket.detail = request.POST['textarea']
            ticket.save()
            return render_to_response('/index/application')

        if request.POST['Submit'] == 'add5':

            ticket = Ticket()
            ticket.type_id = '系统重装'
            ticket.hostname_id = request.POST['host']
            ticket.ip_list = request.POST['ip']
            ticket.idc_id = request.POST['idc']
            ticket.owner_id = request.POST['owner']
            ticket.ip_rac_id = request.POST['ra_ip']
            ticket.raid_id = request.POST['raid']
            ticket.Expectation_time = request.POST['date']
            ticket.create_time = datetime.datetime.now()
            ticket.user_id = request.session['user'].id
            ticket.detail = request.POST['textarea']
            ticket.ticket_status_id = '1'
            ticket.save()
            return redirect('/index/application')

        if request.POST['Submit'] == 'add6':
            
            ticket = Ticket()
            ticket.type_id = '监控更改'
            ticket.hostname_id = request.POST['host']
            ticket.ip_list = request.POST['ip']
            ticket.monitor = request.POST['monitor']
            ticket.owner_id = request.POST['owner']
            ticket.new_oner = request.POST['business']
            ticket.monitor_list = request.POST['list']
            ticket.Expectation_time = request.POST['date']
            ticket.idc_id = request.POST['idc']
            ticket.create_time = datetime.datetime.now()
            ticket.user_id = request.session['user'].id
            ticket.ticket_status_id = '1'
            ticket.detail = request.POST['textarea']
            ticket.save()
            return redirect('/index/application')
    return render_to_response('application.html',{'user' : request.session['user']})

def myapplication_1(request):
    id = request.session['user'].id
    tickets = Ticket.objects.filter(user_id=id)[:10]
    running_tickets = Ticket.objects.filter(user_id=id,ticket_status_id='1')[:10]
    finish_tickets = Ticket.objects.filter(user_id=id,ticket_status_id='3')[:10]
    reject_tickets = Ticket.objects.filter(user_id=id,ticket_status_id='4')[:10]
    new_tickets = Ticket.objects.filter(user_id=id).order_by('-id')[0:1]
    for status_id in new_tickets:
        status_id = status_id.ticket_status_id
        status = Ticket_status.objects.filter(id=status_id)


    if len(tickets) > 0:
        return render_to_response('myapplication_1.html',{'user' : request.session['user'],'tickets' : tickets,'running_tickets' : running_tickets,'finish_tickets':finish_tickets,'reject_tickets':reject_tickets,'status':status})
    else:
        return render(request,'myapplication.html',{'user':request.session['user']})

    
def resource(request):
    if request.POST:
	if request.POST['btnSubmit']=='add':
	    memory = Memory(brand=request.POST['brand'], quantity=request.POST['quantity'],category=request.POST['category'],capacity=request.POST['capacity'],frequency=request.POST['frequency'],check=request.POST['check'],maintainer=request.POST['maintainer'],available=request.POST['available'])
       	    memory.save()
	elif request.POST['btnSubmit']=='update':
	    if request.POST['used_recorder']!='':
		pattern = re.compile(r'\*\d+')
		memory_available = int(request.POST['quantity'])
		for m in pattern.finditer(request.POST['used_recorder']):
		    memory_used=m.group().replace('*','')
		    memory_available=memory_available-int(memory_used)
	    else:
		memory_available = request.POST['available']
	        memory = Memory(id=request.POST['id'],brand=request.POST['brand'], quantity=request.POST['quantity'],category=request.POST['category'],capacity=request.POST['capacity'],frequency=request.POST['frequency'],check=request.POST['check'],maintainer=request.POST['maintainer'],available=memory_available,used_recorder=request.POST['used_recorder'])
		memory.save()
	elif request.POST['btnSubmit']=='delete':
            memory = Memory.objects.get(id=request.POST['id'])
	    memory.delete()
    memorys=Memory.objects.all()
    return render_to_response('resource.html', {'memorys' : memorys,'user' : request.session['user']})



def review(request):
     id = request.session['user'].id
     user = User.objects.get(id=id)
     tickets = Ticket.objects.filter(Q(ticket_status_id='1')|Q(ticket_status_id='2')).order_by('-id')[:15]
     if int(user.role) == 256:
         return render_to_response('review_1.html',{'user' : request.session['user'],'tickets':tickets})
     else:
         return render(request,'review.html',{'user':request.session['user']})

def review_2(request):

    review_id = request.GET.get('key')
    id = request.session['user'].id
    user = User.objects.get(id=id)
    tickets = Ticket.objects.filter(Q(ticket_status_id='1')|Q(ticket_status_id='2')).order_by('-id')[:15]
    if review_id > 0:

        ticket =Ticket.objects.get(id=review_id)

        return render_to_response('review_2.html',{'user' : request.session['user'],'ticket':ticket})
    else:
        return render_to_response('review_1.html',{'user' : request.session['user'],'tickets':tickets})
def review_3(request):
    if request.method == 'POST':
        if request.POST['Submit'] =='add7':
            review_id = request.POST['num']
            a = Ticket.objects.get(id=review_id)
            b = a.ticket_status_id
            if b == 1:
                
                Ticket.objects.filter(id=review_id).update(review=request.POST['textarea'],update_time = datetime.datetime.now(),ticket_status='2')
                return redirect('/index/review_2/')
            if b == 2:
                Ticket.objects.filter(id=review_id).update(review=request.POST['textarea'],update_time = datetime.datetime.now(),ticket_status='3')
                return redirect('/index/review_2/')
        if request.POST['Submit'] =='add8':
            review_id = request.POST['num']
            Ticket.objects.filter(id=review_id).update(review=request.POST['textarea'],update_time = datetime.datetime.now(),ticket_status='4')
            return redirect('/index/review_2/')
def post(request):



   return  render(request,'post.html',{'user' : request.session['user']})
