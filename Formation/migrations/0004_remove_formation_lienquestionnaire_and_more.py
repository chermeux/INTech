# Generated by Django 4.1 on 2022-11-03 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0003_formation_textformation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='LienQuestionnaire',
        ),
        migrations.AlterField(
            model_name='certification',
            name='DateCertificat',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 3, 22, 30, 17, 627746)),
        ),
        migrations.AlterField(
            model_name='formation',
            name='Description',
            field=models.CharField(default=2008, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formation',
            name='Duree',
            field=models.CharField(default=2008, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formation',
            name='NomCertificat',
            field=models.CharField(default=2008, max_length=100),
            preserve_default=False,
        ),
    ]
