from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day(models.Model):
    index = models.TextField(null=False, default="")

    lessnum = models.TextField(null=False, default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # done = models.TextField(null=False, default=0)

    # num = models.TextField(null=False, default=0)

    # to_closest = models.TextField(null=False, default=100)


class Lesson(models.Model):
    name = models.TextField(null=False, default="")

    # deadline = models.DateTimeField(null=True)

    # is_done = models.BooleanField(null=False, default=False)

    # поле со временем, по-умолчанию равное текущему времени (на момент добавления)
    # created_at = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)


class Note(models.Model):
    text = models.TextField(null=False, default="")

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)


class Htask(models.Model):
    text = models.TextField(null=False, default="")

    is_done = models.BooleanField(null=False, default=False)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)


class Event(models.Model):
    text = models.TextField(null=False,default="")

    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)