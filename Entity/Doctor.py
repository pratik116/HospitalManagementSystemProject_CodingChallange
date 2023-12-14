import util.DBConnection as DBConnection
class Doctor(DBConnection.DBConnection):
    prevDrId=105

    def __init__(self,firstName,lastName,specialization,contactNumber):
        self._doctorId=Doctor.prevDrId+1
        Doctor.prevDrId+=1
        self._firstName=firstName
        self._lastName=lastName
        self._specialization=specialization
        self._contactNumber=contactNumber

    def get_doctorId(self):
        return self._doctorId

    def get_firstName(self):
        return self._firstName

    def get_lastName(self):
        return self._lastName

    def get_specialization(self):
        return self._specialization

    def get_contactNumber(self):
        return self._contactNumber

    
    def set_doctorId(self,doctorId):
        self._doctorId=doctorId

    def set_firstName(self,firstName):
        self._firstName=firstName

    def set_lastName(self,lastName):
        self._lastName=lastName

    def set_specialization(self,specialization):
        self._specialization=specialization

    def set_contactNumber(self,contactNumber):
        self._contactNumber=contactNumber

    def print_info(self):
        print(f"Doctor ID: {self._doctorId}")
        print(f"First Name: {self._firstName}")
        print(f"Last Name: {self._lastName}")
        print(f"Specialization: {self._specialization}")
        print(f"Contact Number: {self._contactNumber}")

    def addDoctorIntoTable(self):
        data=[(self._doctorId,self._firstName,self._lastName,self._specialization,self._contactNumber)]        
        insert_str='''insert into Doctor(doctorId,firstName,lastName,specialization,contactNumber)
        values(%s,%s,%s,%s,%s)
    '''
        self.open()
        self.stmt.executemany(insert_str,data)
        self.connection.commit()
        print('New Doctor Enrolled..')
        self.close()
