# Generated by Django 3.0.3 on 2020-03-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_patient'),
        ('doctor', '0010_auto_20200314_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorslots',
            name='is_booked',
        ),
        migrations.RemoveField(
            model_name='doctorslots',
            name='is_requested',
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_requested', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
                ('slot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorSlots')),
            ],
        ),
    ]
