# Generated by Django 3.0.4 on 2020-03-15 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Day')),
            ],
        ),
    ]