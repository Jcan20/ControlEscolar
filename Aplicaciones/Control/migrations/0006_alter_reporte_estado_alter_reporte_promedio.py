# Generated by Django 4.0.6 on 2025-01-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0005_remove_reporte_calificacion_reporte_calificaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='estado',
            field=models.CharField(default='Reprueba', max_length=20),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='promedio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
