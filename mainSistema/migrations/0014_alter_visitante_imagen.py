# Generated by Django 4.0.2 on 2022-05-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSistema', '0013_alter_visitante_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]
