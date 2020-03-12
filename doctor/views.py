from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import doctorDetails

class get_edit_doctorDetails(APIView):
    def get(self,request,):
        doc = doctorDetails.objects.all()
        return Response(doc.values())

    def put(self,request):
        try:
            doc = get_object_or_404(doctorDetails.objects.all(),pk=1)
            doc.full_name = request.data.get('full_name')
            doc.date_of_birth = request.data.get('date_of_birth')
            doc.gender = request.data.get('gender')
            doc.contact_no = request.data.get('contact_no')
            doc.contact_emailid = request.data.get('contact_emailid')
            doc.save()
            return Response({"success":"success"})
        except:
            return Response({"failure":"failure"})