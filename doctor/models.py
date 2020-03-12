from django.db import models
from patient.models import Patient

class doctorDetails(models.Model):
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

class doctorSlots(models.Model):
    time_slots = models.TimeField()
    is_booked = models.CharField(max_length=1,default='N')

class Appointments(models.Model):
    slots = models.OneToOneField(doctorSlots,on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    # anothter firled of doctor will be added in case of multiple doctors
