# Generated by Django 3.2.15 on 2023-09-28 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20230928_1944'),
        ('citas', '0003_auto_20230928_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCita',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.cita')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]