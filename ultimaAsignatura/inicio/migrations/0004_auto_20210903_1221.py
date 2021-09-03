# Generated by Django 3.2.4 on 2021-09-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_empleados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='domicilio',
            field=models.TextField(verbose_name='Domicilio'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='nombreEmpleado',
            field=models.TextField(verbose_name='Nombre del Empleado'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='skills',
            field=models.CharField(max_length=15, verbose_name='Área'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='telefono',
            field=models.CharField(max_length=11, verbose_name='Teléfono'),
        ),
    ]
