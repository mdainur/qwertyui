# Generated by Django 2.2.7 on 2019-12-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20191210_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(),
        ),
    ]
