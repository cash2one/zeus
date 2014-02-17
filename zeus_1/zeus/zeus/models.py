# -*- coding: utf-8 -*-

from django.db import models


class Ticket_status(models.Model):
    class Meta:
        db_table = 'ticket_status'
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=45)
    id_status = models.IntegerField(max_length=5)



class Rack(models.Model):
    class Meta:
        db_table = 'rack'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    location_id = models.IntegerField(max_length=10)
    height = models.IntegerField(max_length=11)
    comment = models.TextField()
    items = models.IntegerField(max_length=11)
    occupation = models.IntegerField(max_length=11)

class Item(models.Model):
    class Meta:
        db_table = 'item'
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField(max_length=3)
    rackmountable = models.IntegerField(max_length=3)
    agent_id = models.IntegerField(max_length=3)
    model =models.CharField(max_length=20)
    size = models.IntegerField(max_length=3)
    sn = models.CharField(max_length=20)
    sn2 = models.CharField(max_length=20)
    servicetag = models.CharField(max_length=20)
    hds = models.IntegerField(max_length=4)
    hd = models.IntegerField(max_length=11)
    raid_id = models.IntegerField(max_length=11)
    ram = models.IntegerField(max_length=11)
    cpumodel = models.CharField(max_length=50)
    cpus = models.IntegerField(max_length=2)
    cores = models.IntegerField(max_length=2)
    purchase_date = models.DateTimeField()
    status_id = models.IntegerField(max_length=2)
    user_id = models.IntegerField(max_length=4)
    owner_id = models.IntegerField(max_length=3)
    location_id = models.IntegerField(max_length=2)
    rack_id = models.IntegerField(max_length=2)
    rack_pos = models.IntegerField(max_length=2)
    application = models.CharField(max_length=45)
    comment = models.TextField()
    label = models.CharField(max_length=50)
    belongto = models.CharField(max_length=50)
    warranty = models.DateTimeField()

class Network(models.Model):
    class Meta:
        db_table = 'network'
    id = models.IntegerField(primary_key=True)
    item = models.ForeignKey(Item)
    mac = models.CharField(max_length=20)
    ipv4 = models.CharField(max_length=20)
    switchid = models.IntegerField(max_length=11)
    switch_port = models.IntegerField(max_length=11)
    eth = models.CharField(max_length=20)
    sshd = models.IntegerField(max_length=11)

class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    access = models.IntegerField()
    user = models.IntegerField()
    owner = models.IntegerField()
    chinese_name = models.CharField(max_length=45)
    role = models.IntegerField()

class Ticket(models.Model):
    class Meta:
        db_table = 'ticket'
    id = models.IntegerField(primary_key=True)
    type_id = models.CharField(max_length=45)
    disk = models.CharField(max_length=45)
    comment=models.CharField(max_length=30)
    memory=models.CharField(max_length=30)
    hostname_id = models.CharField(max_length=30)
    ip_list =  models.CharField(max_length=30)
    sn_id = models.CharField(max_length=30)
    idc_id = models.CharField(max_length=30)
    new_idc = models.CharField(max_length=30) 
    rack_id = models.CharField(max_length=30)
    raid_id =  models.CharField(max_length=30)
    os = models.IntegerField()
    ticket_status = models.ForeignKey(Ticket_status)
    user = models.ForeignKey(User)
    owner_id=models.CharField(max_length=30)
    resource_lists=models.CharField(max_length=45)
    monitor_list=models.CharField(max_length=45)
    monitor=models.CharField(max_length=45)
    host_status = models.CharField(max_length=45)
    variety = models.CharField(max_length=45)
    new_oner = models.CharField(max_length=45)
    ip_rac_id = models.CharField(max_length=25)
    rack_pos = models.CharField(max_length=20)
    detail = models.TextField()
    review = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    Expectation_time = models.DateTimeField()



#class Ticket_status(models.Model):
#    class Meta:
#        db_table = 'ticket_status'
#    id = models.IntegerField(primary_key=True)
#    status = models.CharField(max_length=45)

class Process(models.Model):
    class Meta:
        db_table = 'process'
    id = models.IntegerField(primary_key=True)
    create_time = models.DateTimeField()
    status = models.CharField(max_length=30)
    partition = models.TextField()
    user_id = models.CharField(max_length=30)

class Memory(models.Model):
    class Meta:
    	db_table = 'Memory'
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField()
    capacity = models.CharField(max_length=30)
    check = models.CharField(max_length=50)    	
    frequency = models.CharField(max_length=30)
    maintainer = models.CharField(max_length=50)
    available = models.IntegerField()
    used_recorder = models.CharField(max_length=100)
    category = models.CharField(max_length=30)

