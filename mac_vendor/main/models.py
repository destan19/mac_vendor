from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MacVendor(models.Model):
	mac_prefix = models.CharField(max_length=32)
	vendor_name=models.CharField(max_length=64)	
	
	
