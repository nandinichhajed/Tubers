from django.urls import path
from . import views

urlpatterns = [
    path('contactinfo', views.contactinfo, name="contactinfo"),
    path('socallinks', views.socallinks, name="socallinks"),
]