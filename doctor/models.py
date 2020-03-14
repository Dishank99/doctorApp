from django.db import models
from patient.models import Patient
from django.utils import timezone

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
    slot_date = models.DateField(default=timezone.now())
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()

    def __str__(self):
        return f'{self.slot_start_time} - {self.slot_end_time}'

class Appointments(models.Model):
    slot = models.ForeignKey(doctorSlots,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    is_requested = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    # anothter firled of doctor will be added in case of multiple doctors
