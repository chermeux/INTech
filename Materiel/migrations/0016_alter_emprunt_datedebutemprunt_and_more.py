# Generated by Django 4.1 on 2022-09-11 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materiel', '0015_alter_emprunt_datedebutemprunt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprunt',
            name='DateDebutEmprunt',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 11, 16, 27, 6, 605764)),
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='DateFinEmprunt',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 11, 16, 27, 6, 605764)),
        ),
        migrations.AlterField(
            model_name='objet',
            name='CodeBarre',
            field=models.TextField(null=True),
        ),
    ]
