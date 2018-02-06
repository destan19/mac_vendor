from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import loader,Context
from main.models import *
import json
# Create your views here.
def echo(request):
	return HttpResponse("echo...");
	
def get_mac_vendor(request):
	print 'get_mac_vendor'
	res_json = {};
	mac=request.REQUEST.get("mac")
	print 'mac=',mac
	res_json['vendor'] = "apple"
	return HttpResponse(json.dumps(res_json)) 
