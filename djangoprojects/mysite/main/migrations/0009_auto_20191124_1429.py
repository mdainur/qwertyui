# Generated by Django 2.2.6 on 2019-11-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_food'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
