# Generated by Django 3.2.6 on 2021-09-19 07:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oglasi', '0006_alter_oglas_datum_isteka_oglasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='oglas',
            name='datum_isteka_oglasa',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 9, 40, 4, 410340)),
        ),
    ]
