# Generated by Django 3.0.3 on 2020-05-31 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pid',
        ),
    ]