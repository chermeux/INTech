# Generated by Django 4.1 on 2022-09-11 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materiel', '0004_alter_emprunt_datedebutemprunt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprunt',
            name='DateDebutEmprunt',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 11, 15, 19, 14, 123936)),
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='DateFinEmprunt',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 11, 15, 19, 14, 123936)),
        ),
    ]
