# Generated by Django 4.1.4 on 2022-12-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_pilotqualification_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pilotqualification',
            table='pilots_quals',
        ),
    ]