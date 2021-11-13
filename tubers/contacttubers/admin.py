from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name','email', 'company_name')
    list_display_links = ('full_name', 'id')


admin.site.register(Contact, ContactAdmin)