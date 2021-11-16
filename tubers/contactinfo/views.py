from django.shortcuts import render
from .models import Contactinfo
# Create your views here.

def contactinfo(request):
    contactinfos = Contactinfo.objects.all()
    data = {
        'contactinfos': contactinfos,
    }
    return render(request, 'includes', data)