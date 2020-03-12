from django.urls import path
from .views import AddPatient

urlpatterns = [
    path('register/',AddPatient.as_view(),name='patient-register'),
]