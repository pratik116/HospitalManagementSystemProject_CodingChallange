import util.DBConnection as DBConnection
import Entity.Appointment as A
import Exception.InvalidIdException as InvalidIdException
import Exception.doctorIdNotFound as doctorIdNotFound
import Exception.patientIdNotFound as patientIdNotFound

class IHospitalService(DBConnection.DBConnection):
    def __init__(self):
        pass

    def checkValidAppointmentId(self,appointmentId):
        try:
            self.open()
            self.stmt.execute(f"select * from Appointment where appointmentId={appointmentId}")
            temp=self.stmt.fetchall()
            
            if not temp:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            self.close()

    def checkValidPatientId(self,patientId):
            try:
                self.open()
                self.stmt.execute(f"select * from Patient where patientId={patientId}")
                temp=self.stmt.fetchall()
                if not temp:
                    return False
                else:
                    return True
            except Exception as e:
                print(e)
            finally:
                self.close()

    def checkValiDoctorId(self,doctorId):
            try:
                self.open()
                self.stmt.execute(f"select * from Doctor where doctorId={doctorId}")
                temp=self.stmt.fetchall()
                if not temp:
                    return False
                else:
                    return True
            except Exception as e:
                print(e)
            finally:
                self.close()

    def getAppointmentById(self,appointmentId):
        try:
            if not self.checkValidAppointmentId(appointmentId):
                raise InvalidIdException.InvalidIdException
            else:
                self.open()
                self.stmt.execute(f"Select * From Appointment Where appointmentId={appointmentId}")
                appointment=self.stmt.fetchone()
                return appointment
        except InvalidIdException.InvalidIdException as d:
            print(d)
        except Exception as e:
            print(e)
        finally:
            self.close()
            
    def getAppointmentsForPatient(self,patientId):
        try:
            if not self.checkValidPatientId(patientId):
                raise patientIdNotFound.patientIdNotFound
            else:
                self.open()
                self.stmt.execute(f"Select * From Appointment Where patientId={patientId}")
                appointments=self.stmt.fetchall()
                return appointments 
        except Exception as e:
            print(e)
        finally:
            self.close() 
    
    def getAppointmentsForDoctor(self,doctorId):
        try:
            if not self.checkValiDoctorId(doctorId):
                raise doctorIdNotFound.doctorIdNotFound
            else:
                self.open()
                self.stmt.execute(f"Select * From Doctor Where doctorId={doctorId}")
                appointments=self.stmt.fetchall()
                return appointments
        except doctorIdNotFound.doctorIdNotFound as d:
            print(d) 
        except Exception as e:
            print(e)
        finally:
            self.close()

    
    def scheduleAppointment(self):
        try:
            pid=int(input("Enter Patient Id: "))
            if not self.checkValidPatientId(pid):
                raise patientIdNotFound.patientIdNotFound
            did=int(input("Enter Doctor Id: "))
            if not self.checkValiDoctorId(did):
                raise doctorIdNotFound.doctorIdNotFound
            dt=input("Enter the Date(YYYY-MM-DAY): ")
            des=input("Enter Description: ")
            newappointment=A.Appointment(pid,did,dt,des)
            newappointment.addAppointmentIntoTable()
        except patientIdNotFound.patientIdNotFound as P:
            print(P)
        except doctorIdNotFound.doctorIdNotFound as D:
            print(D)
        except Exception as e:
            print(e)
            
    
    def updateAppointment(self,appointmentId,appointmentDate):
        try:
            if not self.checkValidAppointmentId(appointmentId):
                raise InvalidIdException.InvalidIdException
            else:
                self.open()
                update_str=f'''update Appointment set appointmentDate='{appointmentDate}'
                            where appointmentId={appointmentId}
                            '''
                self.stmt.execute(update_str)
                self.connection.commit()
                print("Appointment Updated...")
        except InvalidIdException.InvalidIdException as I:
            print(I)
        except Exception as e:
            print(e)
        finally:
            self.close()
            
    def cancleAppointment(self,appointmentId):
            try:
                if not self.checkValidAppointmentId(appointmentId):
                    raise InvalidIdException.InvalidIdException
                else:
                    self.open()
                    delete_str=f'''delete from Appointment 
                    where appointmentId={appointmentId}
                    '''
                    self.stmt.execute(delete_str)
                    self.connection.commit()
            except InvalidIdException.InvalidIdException as I:
                print(I)
            except Exception as e:
                print(e)
            else:
                print("Appointment deleted...")
            finally:
                self.close()
