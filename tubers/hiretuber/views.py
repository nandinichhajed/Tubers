from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber
# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        tuber_city = request.POST['tuber_city']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # TODO: do all sanitization
        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, tuber_city=tuber_city, city=city, phone=phone, email=email, state=state, message=message, user_id=user_id )
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('home')