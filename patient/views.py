from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Patient
from doctor.models import doctorSlots,Appointments
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
            return Response({"message":"success"})
        except:
            return Response({"message":"failure"})

    def get(self,request):
        pat = Patient.objects.all()
        return Response(pat.values())

class request_appointment(APIView):
    def post(self,request,pk):
        try:
            pat_id = request.data.get('patient_id')
            slot_id = pk
            print('reached here cp-2')
            check = Appointments.objects.filter(patient_id=pat_id)
            print('reached here cp-1')
            if check  :
                print('reached here cp0')
                return Response({"message":"Requested already"})
            else:
                print('reached here cp1')
                make_request = Appointments()
                print('reached here cp2')
                make_request.patient=(Patient.objects.get(id=pat_id))
                print('reached here cp3')
                make_request.slot=(doctorSlots.objects.get(id=pk))
                print('reached here cp4')
                make_request.is_requested=True
                print('reached here cp5')
                make_request.save()
                print('reached here cp6')
                return Response({"message":"success"})
        except Exception as e:
            return Response({"message":" "+str(e)},content_type='application/json')

class get_patient_appointment_history(APIView):
    def get(self,request,pk):
        #apps = Appointments.objects.all()
        resp = []
        for apps in Appointments.objects.all():
            print('cp1')
            print(apps.patient_id)
            print(apps.is_booked)
            if apps.patient_id == pk and apps.is_booked == True :
                resp.append({
                    "start_time" : (doctorSlots.objects.get(id=apps.slot_id)).slot_start_time,
                    "end_time" : (doctorSlots.objects.get(id=apps.slot_id)).slot_end_time,
                })
        return Response(resp)