from django.contrib import admin
from .models import MacVendor
# Register your models here.
class MacAdmin(admin.ModelAdmin):
	fieldsets=[
		#(None,               {'fields': ['question_text']}),
		#('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(MacVendor,MacAdmin)