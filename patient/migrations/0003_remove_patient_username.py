# Generated by Django 3.0.3 on 2020-03-12 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200310_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
    ]
