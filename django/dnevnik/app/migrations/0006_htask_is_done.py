# Generated by Django 3.0.3 on 2020-03-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='htask',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
