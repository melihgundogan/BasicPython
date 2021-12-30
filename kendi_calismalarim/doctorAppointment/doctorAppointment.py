class Doctor:
    
    def __init__(self, doctorNo, idNumber, name, surname,phoneNumber,eMail):
        self.doctorNo = doctorNo
        self.idNumber = idNumber
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.eMail = eMail

class Patient:
    
    def __init__(self, idNumber, name, surname,phoneNumber,eMail):
        self.idNumber = idNumber
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.eMail = eMail

    def informations(self):
        return self.idNumber + " " + self.name + " " + self.surname + " " + self.phoneNumber + " " + self.eMail

Doctors = open("Doctors.txt", "w")
Appointment = open("Appointment.txt", "w")
Patients = open("Patients.txt", "w")
Appointment.close()
Patients.close()
Doctor1 = "123 23232323232 Ali KUL 507 234 34 34 ali@kul.com\n"
Doctor2 = "124 24242424242 Alper KUL 506 234 34 34 alper@kul.com"   
Doctors.write(Doctor1)
Doctors.write(Doctor2)
Doctors.close()

def patientControl(id):
    Patients = open("Patients.txt", "r")
    contents = Patients.readlines()
    Patients.close()
    
    if len(contents) != 0:
        for i in contents:
            if i[0,12] == id:
                return True
            else:
                return False
    else:
        return False

def appointmentCheck(doctor,date):
    Appointment = open("Appointment.txt", "r")
    contents = Appointment.readlines()
    Appointment.close()

    if len(contents) != 0:
        for i in contents:
            informations = i.split(" ")
            if informations[1] == doctor and informations[2] == date:
                return False
            else:
                return True
    else:
        return True

def patientRegistration():
    name = input("Enter Your Name: ")
    surname = input("Enter Your Surname: ")
    phoneNumber = input("Enter Your Phone Number: ")
    eMail = input("Enter Your E-Mail: ")
    x = Patient(id, name, surname, phoneNumber, eMail)
    Patients = open("Patients.txt", "a")
    Patients.write(x.contents())
    Patients.close()

while True:
    doctorNumber = input("Enter Your Doctor Number: ")
    appointmentDate = input("Enter Your Appointment Date: ")

    if (appointmentCheck(doctorNumber,appointmentDate)):
        print("You can make an appointment.")
        id = input("Enter Your Identification Number: ")
        if(patientControl(id) == False):
            patientRegistration()
            Appointment = open("Appointment.txt", "a")
            Appointment.write(id + " " + doctorNumber + " " + appointmentDate)
            Appointment.close()
            print("Your appointment information has been saved.")
        else:
            print("Your information is registered in our system.")
    else:
        print("Our doctor has an appointment on that date.")