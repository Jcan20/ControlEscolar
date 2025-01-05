# Generated by Django 4.0.6 on 2025-01-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0004_remove_reporte_calificaciones_clase_estudiante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='calificacion',
        ),
        migrations.AddField(
            model_name='reporte',
            name='calificaciones',
            field=models.ManyToManyField(related_name='reportes', to='Control.calificacion'),
        ),
    ]
