from django.shortcuts import render
from .models import Day, Lesson
# Create your views here.


def index(request):
    day = Day.objects.all()
    lessons = []
    for i in day:
        lessons.append(Lesson.objects.filter(project_id = i.id))
    return render(request, 'index.html', {"lessons":lessons, "day":day})

