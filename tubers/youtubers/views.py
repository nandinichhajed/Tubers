from django.shortcuts import render, get_object_or_404
# from .models import Slider, Team
# Create your views here.

def youtubers(request):
    return render(request, 'youtubers/youtubers.html')


def youtuber_detail(request, id):
    tuber = get_object_or_404(youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    return render(request, 'youtubers/search.html')