# Generated by Django 3.0.3 on 2020-05-18 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0006_remove_activity_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
    ]
