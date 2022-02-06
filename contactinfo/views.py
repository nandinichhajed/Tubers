from django.shortcuts import render
from .models import Contactinfo, Socallinks
# Create your views here.

def contactinfo(request):
    contactinfos = Contactinfo.objects.all()
    data = {
        'contactinfos': contactinfos,
    }
    return render(request, 'includes/header.html')

def socallinks(request):
    socallinkss = Socallinks.objects.all()
    data = {
        'socallinkss': socallinkss,
    }
    return render(request, 'includes/footer.html', data)