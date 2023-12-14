import util.DBConnection as DBConnection

class Patient(DBConnection.DBConnection):
    prevPatiendId=7
    def __init__(self,firstName,lastName,dateOfBirth,gender,contactNumber,address):
        self._patientId=Patient.prevPatiendId+1
        Patient.prevPatiendId+=1
        self._firstName=firstName
        self._lastName=lastName
        self._dateOfBirth=dateOfBirth
        self._gender=gender
        self._contactNumber=contactNumber
        self._address=address

    def get_patientId(self):
        return self._patientId

    def get_firstName(self):
        return self._firstName

    def get_lastName(self):
        return self._lastName

    def get_dateOfBirth(self):
        return self._dateOfBirth

    def get_gender(self):
        return self._gender

    def get_contactNumber(self):
        return self._contactNumber

    def get_address(self):
        return self._address

    def set_patientId(self, patientId):
        self._patientId=patientId

    def set_firstName(self, firstName):
        self._firstName=firstName

    def set_lastName(self, lastName):
        self._lastName=lastName

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth=dateOfBirth

    def set_gender(self, gender):
        self._gender=gender

    def set_contactNumber(self, contactNumber):
        self._contactNumber=contactNumber

    def set_address(self, address):
        self._address=address

    def print_info(self):
        print(f"Patient ID: {self._patientId}")
        print(f"First Name: {self._firstName}")
        print(f"Last Name: {self._lastName}")
        print(f"Date of Birth: {self._dateOfBirth}")
        print(f"Gender: {self._gender}")
        print(f"Contact Number: {self._contactNumber}")
        print(f"Address: {self._address}")    
    
    def addPatientIntoTable(self):
        data=[(self._patientId,self._firstName,self._lastName,self._dateOfBirth,self._gender,self._contactNumber,self._address)]
        insert_str='''insert into Patient(patientId,firstName,lastName,dateOfBirth,gender,contactNumber,address)
        values(%s,%s,%s,%s,%s,%s,%s)
        '''
        self.open()
        self.stmt.executemany(insert_str,data)
        self.connection.commit()
        print('Patient Added..')
        self.close()