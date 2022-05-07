# Generated by Django 4.0.4 on 2022-05-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccionSede', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('fechaCreacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=75)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaInauguracion', models.DateTimeField()),
                ('propietario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Futbolista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateTimeField()),
            ],
        ),
    ]
