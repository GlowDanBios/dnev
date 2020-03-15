from django.shortcuts import render, redirect, get_object_or_404
from .models import Day,Lesson, Note, Htask, Event
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        day = Day.objects.all()
        lessons = []
        for i in day:
            lessons.append(Lesson.objects.filter(project_id = i.id))
        return render(request, 'index.html', {"lessons":lessons, "day":day})
    else:
        return redirect('/enter')


def add_lesson(request):
    if request.user.is_authenticated:
        did = request.GET.get("did", None)
        name = request.GET.get('name', None)
        if did and name:
            l = Lesson()
            l.project = get_object_or_404(Day, pk=did)
            l.name = name
            l.save()
        return redirect('/')
    else:
        return redirect('/enter')



def lesson(request):
    if request.user.is_authenticated:
        lid = request.GET.get('lid', None)
        if lid:
            less = get_object_or_404(Lesson, pk=lid)
            note = Note.objects.filter(lesson=less.id)
            h = Htask.objects.filter(lesson=less.id)
            return render(request, 'lesson.html', {'lesson': less, 'htask': h, 'note': note})
        else:
            return redirect('/')
    else:
        return redirect('/enter')


def add_htask(request):
    if request.user.is_authenticated:
        note = request.GET.get("not", None)
        i = request.GET.get("id", None)
        if note:
            n = Htask()
            n.text = note
            n.lesson = get_object_or_404(Lesson, pk=i)
            n.save()
        return redirect(f'/lesson?lid={i}')
    else:
        return redirect('/enter')


def add_note(request):
    if request.user.is_authenticated:
        note = request.GET.get("not", None)
        i = request.GET.get("id", None)
        if note:
            n = Note()
            n.text = note
            n.lesson = get_object_or_404(Lesson, pk=i)
            n.save()
        return redirect(f'/lesson?lid={i}')
    else:
        return redirect('/enter')


def add_htask(request):
    if request.user.is_authenticated:
        t = request.GET.get("not", None)
        i = request.GET.get("id", None)
        if t:
            n = Htask()
            n.text = t
            n.lesson = get_object_or_404(Lesson, pk=i)
            n.save()
        return redirect(f'/lesson?lid={i}')
    else:
        return redirect('/enter')


def delete_lesson(request):
    if request.user.is_authenticated:
        id = request.GET.get("iii", None)
        if id:
            o = get_object_or_404(Lesson, pk=id)
            o.delete()
        return redirect('/')
    else:
        return redirect('/enter')

def add_event(request):
    if request.user.is_authenticated:
        event = request.GET.get("not", None)
        i = request.GET.get("id", None)
        if event:
            e = Event()
            e.text = event
            e.day = get_object_or_404(Day, pk=i)
            e.save()
        return redirect(f'/day?did={i}')
    else:
        return redirect('/enter')


def day(request):
    if request.user.is_authenticated:
        did = request.GET.get('did', None)
        if did:
            day = get_object_or_404(Day, pk=did)
            event = Event.objects.filter(day=day.id)
            return render(request, 'day.html', {'day':day, 'event': event})
        else:
            return redirect('/')
    else:
        return redirect('/enter')


def do(request):
    if request.user.is_authenticated:
        id = request.GET.get('idd', None)
        lid = request.GET.get('lid', None)
        if id and lid:
            ht = get_object_or_404(Htask, pk=id)
            ht.is_done = True
            ht.save()
        return redirect(f'/lesson?lid={lid}')
    else:
        return redirect('/enter')


def clear_d_h(request):
    if request.user.is_authenticated:
        h = Htask.objects.filter(is_done=True)
        for i in h:
            h.delete()
        return redirect('/')
    else:
        return redirect('/enter')


def delete_e(request):
    if request.user.is_authenticated:
        id = request.GET.get("id", None)
        did = request.GET.get("did", None)
        if id:
            e = get_object_or_404(Event, pk=id)
            e.delete()
        return redirect(f'/day?did={did}')
    else:
        return redirect('/enter')


def delete_n(request):
    if request.user.is_authenticated:
        id = request.GET.get("id", None)
        lid = request.GET.get("lid", None)
        if id:
            n = get_object_or_404(Note, pk=id)
            n.delete()
        return redirect(f'/lesson?lid={lid}')
    else:
        return redirect('/enter')


def reg(request):
    log = request.GET.get('log', None)
    pwd = request.GET.get('pwd', None)
    if log and pwd:
        if User.objects.filter(username=log):
            messages.info(request, "Существует пользователь с таким логином.")
            return redirect('/enter')
        else:
            u = User.objects.create_user(log)
            u.set_password(pwd)
            u.save()
            return redirect('/enter')
    return redirect('/enter')


def enter(request):
    return render(request, 'auth.html')


def logut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/enter')
    else:
        return redirect('/enter')


def log(request):
    log = request.GET.get('log', None)
    pwd = request.GET.get('pwd', None)
    if log and pwd:
        user = authenticate(request, username=log, password=pwd)
        if user is not None:
            print(1)
            login(request, user)
            return redirect('/')
        else:
            # messages.info("неверный логин или пароль")
            return redirect('/enter')
    return redirect('/enter')