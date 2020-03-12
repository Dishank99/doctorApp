from rest_framework.serializers import ModelSerializer
from .models import Patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'username',
            'full_name',
            'date_of_birth',
            'gender',
            'contact_no',
            'contact_emailid'
        ]