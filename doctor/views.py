from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import doctorDetails,doctorSlots,Appointments

class get_edit_doctorDetails(APIView):
    def get(self,request):
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
            return Response({"message":"success"})
        except:
            return Response({"message":"failure"})

class get_set_slots(APIView):
    def get(self,request):
        docSlots = doctorSlots.objects.all()
        return Response(docSlots.values())
    
    def post(self,request):
        try:
            start_time = request.data.get('start_time')
            end_time = request.data.get('end_time')
            slots = doctorSlots()
            slots.slot_start_time=start_time
            slots.slot_end_time=end_time
            slots.save()
            return Response({"message":"success"})
        except:
            return Response({"message":"failure"})

class get_requested_appointments(APIView):
    def get(self,request):
        # requested_appointments = Appointments.objects.all().filter(is_requested=True)
        # return Response(requested_appointments.values())
        requested_appointments=[]
        for appointments in Appointments.objects.all():
            if appointments.is_requested == True and appointments.is_booked == False:
                requested_appointments.append(appointments)
        return Response(requested_appointments)

class confirm_appointment(APIView):
    def put(self,request,pk):
        try:
            to_confirm = Appointments.objects.get(patient_id=pk)
            if to_confirm.is_requested == True:
                to_confirm.is_booked = True
                to_confirm.save()
                return Response({"message":"success"})
            return Response({"message":"failure"})
        except:
            return Response({"message":"failure"})

    def get(self,request,pk=None):
        apps = Appointments.objects.all()
        return Response(apps.values())

class get_booked_appointments(APIView):
    def get(self,request):
        booked_appoinments = Appointments.objects.all().filter(is_booked=True)
        return Response(booked_appoinments.values())