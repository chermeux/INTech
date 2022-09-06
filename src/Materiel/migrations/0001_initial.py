# Generated by Django 4.1 on 2022-08-31 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idObjetEmprunt', models.PositiveIntegerField(blank=True, null=True)),
                ('NomEmprunteur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Objet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CodeBarre', models.TextField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('DateDebutEmprunt', models.DateField(blank=True, default=datetime.datetime(2022, 8, 31, 22, 34, 49, 642400))),
                ('DateFinEmprunt', models.DateField(blank=True, default=datetime.datetime(2022, 8, 31, 22, 34, 49, 642400))),
            ],
        ),
    ]
