# Generated by Django 4.1 on 2022-11-04 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0005_remove_formation_pdfformationecrite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='DateCertificat',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 4, 10, 14, 13, 452977)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='idFormation',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='certification',
            name='idPersonneCertificat',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]