# Generated by Django 2.2.6 on 2019-11-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_dob',
        ),
    ]