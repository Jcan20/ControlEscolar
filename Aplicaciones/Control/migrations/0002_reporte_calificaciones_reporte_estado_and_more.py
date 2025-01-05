# Generated by Django 4.0.6 on 2024-12-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='calificaciones',
            field=models.ManyToManyField(related_name='reportes', to='Control.calificacion'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='estado',
            field=models.CharField(default='Reprueba', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='promedio',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=4),
        ),
    ]
