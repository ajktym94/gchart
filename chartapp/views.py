from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from django.shortcuts import render_to_response
from .models import Response
import urllib2
from chartapp.models import Response
from chartapp.models import Count
#import pdb; pdb.set_trace()

from django.core import serializers
# Create your views here.

def index(request):
	request_headers = {'x-api-key': 'c2ee00db1a75428981d49a5c74d24015'}


	for i in range(1,20):
		requestt = urllib2.Request("https://fulfil_demo.fulfil.io/api/v1/model/sale.sale?field=reference&field=shipment_address.subdivision.code&field=shipment_address.country.code&filter=[[\"state\",\"=\",\"processing\"]]&page="+`i`, headers=request_headers)
		opener = urllib2.build_opener()
		f = opener.open(requestt)
		jsonf=json.loads(f.read())
		for resp in jsonf:
			r=Response()
			r.recname=resp["rec_name"]
			r.reference=resp["reference"]
			r.idf=resp["id"]
			r.state=resp["shipment_address.subdivision.code"]
			r.country=resp["shipment_address.country.code"]
			r.save()
			
	r=Response.objects.all()
	
	for i in r:
		#cn=0
		n=Count()
		n.sname=i.state;
		n.scount=Response.objects.filter(state=i.state).count()
		
		'''for j in r:
									if (j.state)==(i.state):
										cn=cn+1
									
								n.scount=cn	'''
		
		n.save()
	
	
	c=Count.objects.all()
	
	for i in c:
					print i.sname	
					print i.scount
	#r.delete()	
	#c.delete()
	context={'c':c,}
	Count.objects.all().delete()
	Response.objects.all().delete()
	
	template=loader.get_template('chartapp/index.html') 

	return HttpResponse(template.render(context,request))

