# Generated by Django 4.1.4 on 2022-12-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LOX',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('prsn_id', models.IntegerField()),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'lox',
                'managed': False,
            },
        ),
    ]