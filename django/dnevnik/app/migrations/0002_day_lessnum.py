# Generated by Django 3.0.3 on 2020-03-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='lessnum',
            field=models.TextField(default=0),
        ),
    ]
