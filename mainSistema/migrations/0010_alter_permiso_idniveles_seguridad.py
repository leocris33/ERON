# Generated by Django 4.0.2 on 2022-05-12 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainSistema', '0009_alter_permiso_fecha_fin_alter_permiso_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='idNiveles_seguridad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainSistema.niveles_seguridad'),
        ),
    ]
