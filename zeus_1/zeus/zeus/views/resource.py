from django.shortcuts import render_to_response,HttpResponse
from zeus.models import Memory
import re
import simplejson

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
	return render_to_response('resource.html', {'memorys' : memorys})	

def ajax(request):
    data = {}
    #req = simplejson.loads(request.raw_post_data)
    value = request.POST.get("hello")

    #print type(req)
    #dict['name'] = 'hello'
    #print type(dict)
    data["lit"] = value
    json=simplejson.dumps(data)
    #print type(json)
    #return render_to_response('resource.html', {'dict' : dict})
    return HttpResponse(json)
