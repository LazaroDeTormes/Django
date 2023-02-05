# Generated by Django 4.1.2 on 2023-02-03 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_alter_articulo_fecha_venta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_venta',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 39, 25, 594607), verbose_name='Fecha de venta'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_tor_emp',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 39, 25, 593610), verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_tor_fin',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 39, 25, 593610), verbose_name='Fecha de finiquito'),
        ),
    ]