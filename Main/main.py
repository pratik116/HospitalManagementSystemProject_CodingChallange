import util.DBConnection as DBConnection
import Entity.Patient as P
import Entity.Appointment as A
import Entity.Doctor as D
import Entity.CreateTable as C
import dao.Functionalities as Functionalities



#Here I entered the dummy data in the mysql and also insert data in mysql using python in main method
def main():
    conn=DBConnection.DBConnection()
    conn.open()
    C.createPatientTable()
    C.createDoctorTable()
    C.createAppointmentTable()

    # Dummy records inserted in database by python
    
    # patient=P.Patient("Pratik","Wani",'2002-03-10','M','9022183434',"Vijay Nagar,Nashik, Maharashtra")
    # patient.addPatientIntoTable()

    # doctor=D.Doctor("Bhushan","Jagtap","Cardiologist","9087654321")
    # doctor.addDoctorIntoTable()

    # apointment1=A.Appointment(1,101,'2023-12-30',"Pain in Hand")
    # apointment1.addAppointmentIntoTable()

    
    
    New_Hospital=Functionalities.IHospitalService()
    
    while True:
        try:
            print("\n****Welcome User*****\n")
            print("Press 1 to Check Appointment Details using Appointment ID")
            print("Press 2 to Check Appointment Details using Patient ID")
            print("Press 3 to Check scheduled Appointments of Doctors")
            print("Press 4 to Schedule new Appointment")
            print("Press 5 to Update the Scheduled Appointment")
            print("Press 6 to Cancle the Appointment")
            print("Press 7 to exit")
            check = int(input("Enter Here: "))
            if check==1:
                Id=int(input("Please Enter your Appointment Id: "))
                temp=New_Hospital.getAppointmentById(Id)
                for i in temp:
                    print(i)

            elif check==2:
                Id=int(input("Please Enter your Patient Id: "))
                temp=New_Hospital.getAppointmentsForPatient(Id)
                for i in temp:
                    print(i)

            elif check==3:
                Id=int(input("Please Enter your Doctor Id: "))
                temp=New_Hospital.getAppointmentsForDoctor(Id)
                for i in temp:
                    print(i)
            
            elif check==4:
                New_Hospital.scheduleAppointment()

            elif check==5:
                new_date=input("Enter the new date: ")
                appId=input("Enter the Appointment ID: ")
                New_Hospital.updateAppointment(appId,new_date)

            elif check==6:
                Id=int(input("Please Enter your Appointment Id: "))
                New_Hospital.cancleAppointment(Id)
            elif check==7:
                print("Thank You User")
                break
            else:
                print("\nInvalid Option")
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    main()