# Generated by Django 4.0.6 on 2024-12-31 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0002_reporte_calificaciones_reporte_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='promedio',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=4),
        ),
    ]
