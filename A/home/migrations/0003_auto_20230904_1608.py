# Generated by Django 3.2.20 on 2023-09-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_todo_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
