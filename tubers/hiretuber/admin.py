from django.contrib import admin
from .models import Hiretuber
# from django.utils.html import format_html


class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email','tuber_name')
    list_display_links = ('first_name', 'id')


admin.site.register(Hiretuber, HiretuberAdmin)