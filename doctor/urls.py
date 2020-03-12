from django.urls import path
from .models import doctorDetails
from .views import get_edit_doctorDetails

urlpatterns = [
    path('info/',get_edit_doctorDetails.as_view(),name='doctor-info'),
]