from django.urls import path
from .models import doctorDetails
from .views import (get_edit_doctorDetails,get_set_slots,
                    get_requested_appointments,confirm_appointment,get_booked_appointments)

urlpatterns = [
    path('info/',get_edit_doctorDetails.as_view(),name='doctor-info'),
    path('slots/',get_set_slots.as_view(),name='doctor-slots'),
    path('requests/',get_requested_appointments.as_view(),name='doctor-requested-appointments'),
    path('confirm/<int:pk>/',confirm_appointment.as_view(),name='doctor-confirm-appointment'),
    path('booked/',get_booked_appointments.as_view(),name='docotr-booked-appointments'),
]