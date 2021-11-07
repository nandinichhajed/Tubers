from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    # path('contact', views.contact, name='contact'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    # path('youtubers', views.youtubers, name='youtubers'),
    # path('search', views.search, name='search'),
    # path('dashboard', views.dashboard, name='dashboard'),
]