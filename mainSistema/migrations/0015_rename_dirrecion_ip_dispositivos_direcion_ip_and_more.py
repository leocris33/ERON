# Generated by Django 4.0.2 on 2022-05-13 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSistema', '0014_alter_visitante_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivos',
            old_name='dirrecion_ip',
            new_name='direcion_ip',
        ),
        migrations.RenameField(
            model_name='dispositivos',
            old_name='dirrecion_mac',
            new_name='direcion_mac',
        ),
    ]
