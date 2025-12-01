# Create a Hospital system with Doctor, Patient, and Appointment classes.
# Implement methods to schedule appointments and print a daily appointment list.

class Doctor:
    def __init__(self,name):
        self.name =  name

class Patient:
    def __init__(self,name):
        self.name = name

class Appointment:
    def __init__(self,doctor,patient,time):
        self.doctor = doctor
        self.patient = patient
        self.time = time

class HospitalSystem:
    def __init__(self):
        self.appointements = []

    def schedule_appointment(self,doctor,patient,time):
        appt = Appointment(doctor,patient,time)
        self.appointements.append(appt)
        print(f"Appointment Scheduled : {patient.name} with Dr. {doctor.name} at {time}")

    def print_daily_appointment(self):
        print("Daily Appointments : ")
        if not self.appointements:
            print("No appointements!")
        else:
            for appt in self.appointements:
                print(f"{appt.time} - {appt.patient.name} with Dr . {appt.doctor.name}")

doc1 = Doctor("Smith")
doc2 = Doctor("Johnson")

pat1 = Patient("Alice")
pat2 = Patient("bob")

hospital = HospitalSystem()
hospital.schedule_appointment(doc1,pat1,"10.00 A.M")
hospital.schedule_appointment(doc2,pat2,"2.00 P.M")
hospital.print_daily_appointment()