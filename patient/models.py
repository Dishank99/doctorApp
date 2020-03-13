from django.db import models
import datetime

class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender_choices = (
        ('M','male'),
        ('F','female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1,choices=gender_choices)
    contact_no = models.IntegerField()
    contact_emailid = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

#class Appointments(models.Model):


