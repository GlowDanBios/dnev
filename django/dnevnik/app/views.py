from django.shortcuts import render, redirect, get_object_or_404
from .models import Day,Lesson, Note, Htask, Event

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
    if lid:
        less = get_object_or_404(Lesson, pk=lid)
        note = Note.objects.filter(lesson=less.id)
        h = Htask.objects.filter(lesson=less.id)
        return render(request, 'lesson.html', {'lesson': less, 'htask': h, 'note': note})
    else:
        return redirect('/')


def add_htask(request):
    note = request.GET.get("not", None)
    i = request.GET.get("id", None)
    if note:
        n = Htask()
        n.text = note
        n.lesson = get_object_or_404(Lesson, pk=i)
        n.save()
    return redirect(f'/lesson?lid={i}')


def add_note(request):
    note = request.GET.get("not", None)
    i = request.GET.get("id", None)
    if note:
        n = Note()
        n.text = note
        n.lesson = get_object_or_404(Lesson, pk=i)
        n.save()
    return redirect(f'/lesson?lid={i}')


def add_htask(request):
    t = request.GET.get("not", None)
    i = request.GET.get("id", None)
    if t:
        n = Htask()
        n.text = t
        n.lesson = get_object_or_404(Lesson, pk=i)
        n.save()
    return redirect(f'/lesson?lid={i}')


def delete_lesson(request):
    id = request.GET.get("iii", None)
    if id:
        o = get_object_or_404(Lesson, pk=id)
        o.delete()
    return redirect('/')

def add_event(request):
    event = request.GET.get("not", None)
    i = request.GET.get("id", None)
    if event:
        e = Event()
        e.text = event
        e.day = get_object_or_404(Day, pk=i)
        e.save()
    return redirect(f'/day?did={i}')


def day(request):
    did = request.GET.get('did', None)
    if did:
        day = get_object_or_404(Day, pk=did)
        event = Event.objects.filter(day=day.id)
        return render(request, 'day.html', {'day':day, 'event': event})
    else:
        return redirect('/')


def do(request):
    id = request.GET.get('idd', None)
    lid = request.GET.get('lid', None)
    if id and lid:
        ht = get_object_or_404(Htask, pk=id)
        ht.is_done = True
        ht.save()
    return redirect(f'/lesson?lid={lid}')
