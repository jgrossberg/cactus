# Generated by Django 2.1.7 on 2019-03-02 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190302_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
