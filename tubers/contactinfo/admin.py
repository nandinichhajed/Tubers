from django.contrib import admin
from .models import Contactinfo
# Register your models here.

class ContactinfoAdmin(admin.ModelAdmin):

    list_display = ('id','email', 'phone')
    list_display_links = ('email', 'id')
    
admin.site.register(Contactinfo, ContactinfoAdmin)