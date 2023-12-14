import util.DBConnection as DBConnection

class Appointment(DBConnection.DBConnection):
    prevAppointment=1010

    def __init__(self,patientId,doctorId,appointmentDate,description):
        self._appointmentId=Appointment.prevAppointment+1
        Appointment.prevAppointment+=1
        self._patientId=patientId
        self._doctorId=doctorId
        self._appointmentDate=appointmentDate
        self._description=description

    def get_appointmentId(self):
        return self._appointmentId

    def get_patientId(self):
        return self._patientId

    def get_doctorId(self):
        return self._doctorId

    def get_appointmentDate(self):
        return self._appointmentDate

    def get_description(self):
        return self._description

    
    def set_appointmentId(self,appointmentId):
        self._appointmentId=appointmentId

    def set_patientId(self,patientId):
        self._patientId=patientId

    def set_doctorId(self,doctorId):
        self._doctorId=doctorId

    def set_appointmentDate(self,appointmentDate):
        self._appointmentDate=appointmentDate

    def set_description(self,description):
        self._description=description

    def print_info(self):
        print(f"Appointment ID: {self._appointmentId}")
        print(f"Patient ID: {self._patientId}")
        print(f"Doctor ID: {self._doctorId}")
        print(f"Appointment Date: {self._appointmentDate}")
        print(f"Description: {self._description}")
    
    def addAppointmentIntoTable(self):
        data=[(self._appointmentId,self._patientId,self._doctorId,self._appointmentDate,self._description)] 

        insert_str='''insert into Appointment(appointmentId,patientId,doctorId,appointmentDate,description)
        values(%s,%s,%s,%s,%s)
        '''
        self.open()
        self.stmt.executemany(insert_str,data)
        self.connection.commit()
        print('Appointment Scheduled...')
        self.close()
