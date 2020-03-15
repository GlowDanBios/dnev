from django.shortcuts import render
from .models import Day,Lesson

# Create your views here.


def index(request):
    days = Day.objects.all()
    return render(request, 'index.html')
