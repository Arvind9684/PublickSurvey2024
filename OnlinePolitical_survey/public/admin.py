from django.contrib import admin
from .models import contact_detail,chat_detail,public_votting

# Register your models here.
class contact_detailsAdmin(admin.ModelAdmin):
    list_display=['mobile','country','city','date','time']
admin.site.register(contact_detail,contact_detailsAdmin)

class chat_detailsAdmin(admin.ModelAdmin):
    list_display=['mobile','country','city','Chat','Latitude','Longitude','date','time']
admin.site.register(chat_detail,chat_detailsAdmin)


class public_vottingAdmin(admin.ModelAdmin):
    list_display=['mobile','country','city','party_name','Latitude','Longitude','date','time','result']
admin.site.register(public_votting,public_vottingAdmin)
