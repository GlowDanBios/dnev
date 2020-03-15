from django.shortcuts import render, redirect, get_object_or_404
from .models import Day,Lesson, Note

# Create your views here.


def index(request):
    day = Day.objects.all()
    lessons = []
    for i in day:
        lessons.append(Lesson.objects.filter(project_id = i.id))
    return render(request, 'index.html', {"lessons":lessons, "day":day})


def add_lesson(request):
    did = request.GET.get("did", None)
    name = request.GET.get('name', None)
    if did and name:
        l = Lesson()
        l.project = get_object_or_404(Day, pk=did)
        l.name = name
        l.save()
    return redirect('/')


def lesson(request):
    lid = request.GET.get('lid', None)
    print(lid)
    if lid:
        less = get_object_or_404(Lesson, pk=lid)
        note = Note.objects.filter(lesson=less.id)
        return render(request, 'lesson.html', {'lesson':less, 'note': note})
    else:
        return redirect('/')