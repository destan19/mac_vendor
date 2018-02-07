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
	res_json = {};
	mac = request.GET.get("mac");
	print 'mac=',mac
	mac_prefix=mac[0:8]
	res_json['mac'] = mac[0:8]
	res_json['vendor'] = "not exist"
	entry=MacVendor.objects.filter(mac_prefix=mac[0:8])[0]
	if entry is None:
		print 'not find entry',mac
	else:
		res_json['vendor'] = entry.vendor_name
	return HttpResponse(json.dumps(res_json)) 

	
def init_mac_database(request):
	res_json = {};
	fd= open("./vendor_mac.ini","r")
	cur_vendor=""
	while 1:
		line=fd.readline();
		if len(line)<=0:
			break;
		if -1 != line.find("#start"):
			cur_vendor=line[7:]
			continue
		if -1 != line.find("#"):
			continue
		mac_prefix = line.strip();
		mac_prefix=mac_prefix.replace("-",":");
		print "insert %s,%s"%(mac_prefix,cur_vendor)
		entry=MacVendor()
		entry.mac_prefix=mac_prefix
		entry.vendor_name=cur_vendor
		entry.save()
	fd.close()
	return HttpResponse(json.dumps(res_json)) 