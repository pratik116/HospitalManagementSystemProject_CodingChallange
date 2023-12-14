import util.DBConnection as DBConnection

create=DBConnection.DBConnection()
def createPatientTable():
        create_str='''create  table  if not exists Patient(patientId int primary key,
        firstName varchar(50),
        lastName varchar(50),
        dateOfBirth date,
        gender char(1),
        contactNumber varchar(11),
        address varchar(100)
        )'''
        create.open()
        create.stmt.execute(create_str)
        create.stmt.close()
        print('Table created.....')

def createDoctorTable():
        create_str='''create  table  if not exists Doctor(doctorId int primary key,
        firstName varchar(50),
        lastName varchar(50),
        specialization varchar(50),
        contactNumber varchar(11)
        )'''
        create.open()
        create.stmt.execute(create_str)
        create.stmt.close()
        print('Table created.....')

def createAppointmentTable():
        create_str='''create  table  if not exists Appointment(appointmentId int primary key,
        patientId int references Patient(patientId),
        doctorId int references Doctor(doctorId),
        appointmentDate date,
        description varchar(100)
        )'''
        create.open()
        create.stmt.execute(create_str)
        create.stmt.close()
        print('Table created.....')