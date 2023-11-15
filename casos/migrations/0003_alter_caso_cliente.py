# Generated by Django 3.2.15 on 2023-09-28 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_clientes_cliente'),
        ('casos', '0002_rename_casos_caso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
    ]
