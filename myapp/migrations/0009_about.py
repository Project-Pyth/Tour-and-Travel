# Generated by Django 3.0.3 on 2020-05-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('eid', models.EmailField(max_length=225)),
                ('city', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
