# Generated by Django 3.0.3 on 2020-05-10 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_cab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='message',
            new_name='subject',
        ),
    ]