"""dnevnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, add_lesson, lesson, add_note, delete_lesson, add_htask, add_event, day, do, delete_n, delete_e, clear_d_h

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_lesson/', add_lesson),
    path('lesson', lesson),
    path('add_note', add_note),
    path('add_htask', add_htask),
    path('delete_lesson', delete_lesson),
    path('day', day),
    path('add_event', add_event),
    path('do', do),
    path('delete_n', delete_n),
    path('delete_e', delete_e),
    path('clear_d_h', clear_d_h),
]
