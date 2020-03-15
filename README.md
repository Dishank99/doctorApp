# doctorApp
# This app enables patient to registers his or hers details.
# Since, it is an App for doctor, he can edit his or her information as well.
# It mainly focuses on registering appointments for patient
# For registering an appointment :-
  • Patient can view the unbooked slots
  • He can can only reqyest for an appointments
  • Doctor can see the requested appointments and confrims the request of a patient which will mark appointment as booked
  • Once the appointment is booked, the patient can see all the past booked apoointments
# Doctor has to first set the slots. The date he sets the slot is only considered.

# api slugs
  • /patient/register/ : to register patient
  • /doctor/info/ : edit doctir info
  • /doctor/slots/ : set slot for current date
  • /patient/available/ : patient can view all unbooked appointments
  • /patient/request/<slot id> : patient can request a particular slot. A patient can request only once
  • /doctor/requests/ : doctor can view the appointment requests
  • /doctor/confirm/<patient id> : doctor can confirm the appointment of a particular patient
  • /patient/history/<patient id> : patient can view his past booked appointments
