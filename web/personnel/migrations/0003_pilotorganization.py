# Generated by Django 4.1.4 on 2022-12-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='PilotOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'pilots_orgs',
                'managed': False,
            },
        ),
    ]