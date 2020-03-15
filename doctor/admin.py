from django.contrib import admin
from .models import doctorDetails,doctorSlots,Appointments

admin.site.register(doctorDetails)
admin.site.register(doctorSlots)
admin.site.register(Appointments)
