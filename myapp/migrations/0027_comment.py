# Generated by Django 3.0.3 on 2020-06-01 11:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0026_auto_20200531_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_comment', models.DateField(default=datetime.date.today)),
                ('message', models.TextField(verbose_name='Message')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TourPost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]