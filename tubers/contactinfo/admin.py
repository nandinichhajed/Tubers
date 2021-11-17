from django.contrib import admin
from .models import Contactinfo, Socallinks
# Register your models here.

class ContactinfoAdmin(admin.ModelAdmin):

    list_display = ('id','email', 'phone')
    list_display_links = ('email', 'id')
    
admin.site.register(Contactinfo, ContactinfoAdmin)

class SocallinksAdmin(admin.ModelAdmin):
    
    list_display = ('id','fb_link', 'insta_link', 'twitter_link', 'yt_link')
    list_display_links = ('fb_link', 'id')
    
admin.site.register(Socallinks, SocallinksAdmin)