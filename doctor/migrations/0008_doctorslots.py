# Generated by Django 3.0.3 on 2020-03-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20200313_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_start_time', models.TimeField()),
                ('slot_end_time', models.TimeField()),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
    ]
