from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Patient
from rest_framework import serializers
from .serializer import PatientSerializer

class AddPatient(APIView):
    # def post(self,request):
    #     user_name = request.data.get('full_name')
    #     if Patient.objects.filter(full_name=user_name).first():
    #         return Response({"failure":"User alreay exists"})
    #     else:
    #         pat = Patient()
    #         pat.full_name = user_name
    #         pat.date_of_birth = request.data.get('date_of_birth')
    #         pat.gender = request.data.get('gender')
    #         pat.contact_no = request.data.get('contact_no')
    #         pat.contact_emailid = request.data.get('contact_emailid')
    #         pat.save()

    def post(self,request):
        try:
            pat = Patient()
            pat.full_name = request.data.get('full_name')
            pat.date_of_birth = request.data.get('date_of_birth')
            pat.gender = request.data.get('gender')
            pat.contact_no = request.data.get('contact_no')
            pat.contact_emailid = request.data.get('contact_emailid')
            pat.save()
            return Response({"sucess":"sucess"})
        except:
            return Response({"failure":"failure"})

    def get(self,request):
        pat = Patient.objects.all()
        return Response(pat.values())
