from django.urls import path
from .views import AddPatient,request_appointment,get_patient_appointment_history

urlpatterns = [
    path('register/',AddPatient.as_view(),name='patient-register'),
    path('request/<int:pk>/',request_appointment.as_view(),name='patient-request-appointment'),
    path('history/<int:pk>/',get_patient_appointment_history.as_view(),name='patient-appointment-history'),
]