# Generated by Django 4.1.2 on 2023-02-03 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0009_torneo_fecha_tor_emp_torneo_fecha_tor_fin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=100)),
                ('fecha_venta', models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 6, 19, 293439), verbose_name='Fecha de venta')),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='static/media'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_tor_emp',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 6, 19, 293439), verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='fecha_tor_fin',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 6, 19, 293439), verbose_name='Fecha de finiquito'),
        ),
    ]
