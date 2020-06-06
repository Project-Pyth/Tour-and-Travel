# Generated by Django 3.0.3 on 2020-05-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_book_mid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]
