# Generated by Django 3.0.3 on 2020-05-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20200516_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpost',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]