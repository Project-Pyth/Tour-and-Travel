# Generated by Django 3.0.3 on 2020-05-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20200530_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('depart_date', models.DateField()),
                ('arrive_date', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]