# Generated by Django 3.2.15 on 2023-09-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=100)),
                ('apellido', models.TextField(max_length=100)),
                ('fecha_Nac', models.DateTimeField(verbose_name='Fecha Nacimiento')),
                ('sexo', models.TextField(max_length=20)),
                ('documento', models.FileField(blank=True, null=True, upload_to='documentos/casos')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]