# Generated by Django 3.2.20 on 2023-08-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
