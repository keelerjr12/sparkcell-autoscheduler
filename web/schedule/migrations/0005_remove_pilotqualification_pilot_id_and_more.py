# Generated by Django 4.1.4 on 2022-12-15 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_pilotqualification_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pilotqualification',
            name='pilot_id',
        ),
        migrations.RemoveField(
            model_name='pilotqualification',
            name='qual_id',
        ),
        migrations.DeleteModel(
            name='Pilot',
        ),
        migrations.DeleteModel(
            name='PilotQualification',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
    ]
