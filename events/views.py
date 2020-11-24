from django.shortcuts import render
from .models import Event

# Create your views here.


def home(request):
    events = Event.objects  # получаем все объекты из базы данных на страницу home.html
    return render(request, 'events/home.html', {'events': events})
