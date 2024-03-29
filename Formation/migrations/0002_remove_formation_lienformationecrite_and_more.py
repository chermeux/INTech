# Generated by Django 4.1 on 2022-11-03 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='LienFormationEcrite',
        ),
        migrations.AddField(
            model_name='formation',
            name='PDFFormationEcrite',
            field=models.FileField(default=2008, upload_to='file'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certification',
            name='DateCertificat',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 3, 14, 58, 20, 818384)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='idFormation',
            field=models.IntegerField(default=2008),
            preserve_default=False,
        ),
    ]
