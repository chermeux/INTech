# Generated by Django 4.1 on 2022-11-03 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NomCertificat', models.TextField(null=True)),
                ('Description', models.TextField(null=True)),
                ('Duree', models.TextField(null=True)),
                ('LienQuestionnaire', models.TextField(null=True)),
                ('LienFormationEcrite', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idPersonneCertificat', models.IntegerField()),
                ('EtatCertification', models.TextField(choices=[('DemandeValidation', 'DemandeValidation'), ('Validee', 'Validee'), ('', '')], null=True)),
                ('DateCertificat', models.TextField(null=True)),
                ('idFormation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Formation.formation')),
            ],
        ),
    ]
