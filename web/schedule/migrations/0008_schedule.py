# Generated by Django 4.1.4 on 2023-01-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_duty_dutytype_shellduty_alter_line_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('submission_date_time', models.DateTimeField()),
                ('status', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'schedule',
                'managed': False,
            },
        ),
    ]
