# Generated by Django 3.2.15 on 2023-09-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_rename_citas_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='Descripcion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='Nombre_Persona',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cita',
            name='motivo',
            field=models.CharField(max_length=100),
        ),
    ]