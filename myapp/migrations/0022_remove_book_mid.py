# Generated by Django 3.0.3 on 2020-05-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='mid',
        ),
    ]
