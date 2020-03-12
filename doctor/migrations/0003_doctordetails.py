# Generated by Django 3.0.3 on 2020-03-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0002_delete_doctordetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'Other')], max_length=1)),
                ('contact_no', models.IntegerField()),
                ('contact_emailid', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
