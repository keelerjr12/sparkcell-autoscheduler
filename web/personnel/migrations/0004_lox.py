# Generated by Django 4.1.4 on 2022-12-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_pilotorganization'),
    ]

    operations = [
        migrations.CreateModel(
            name='LOX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vw_pilots_quals',
                'managed': False,
            },
        ),
    ]
