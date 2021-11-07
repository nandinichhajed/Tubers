from django.shortcuts import render
from .models import Slider, Team
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    data = {
        'sliders': sliders,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')

# def login(request):
#     return render(request, 'accounts/login.html')

# def register(request):
#     return render(request, 'accounts/register.html')

# def dashboard(request):
#     return render(request, 'accounts/dashboard.html')

# def logout(request):
#     return render(request, 'accounts/logout.html')
