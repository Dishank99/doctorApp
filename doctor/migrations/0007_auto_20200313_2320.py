# Generated by Django 3.0.3 on 2020-03-13 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20200313_2307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointments',
        ),
        migrations.DeleteModel(
            name='doctorSlots',
        ),
    ]