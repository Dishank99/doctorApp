# Generated by Django 3.0.3 on 2020-03-13 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_patient'),
        ('doctor', '0013_auto_20200314_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]