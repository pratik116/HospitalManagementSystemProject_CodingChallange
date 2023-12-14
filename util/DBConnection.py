import mysql.connector as sql
import util.PropertyUtil as PropertyUtil
class DBConnection:
    def open(self):
        try:
            # conn=PropertyUtil.getPropertyString()
            self.connection=sql.connect(host="localhost",database="HospitalManagement",username="root",password="JEEjee@116")
            self.stmt=self.connection.cursor()
            if self.connection.is_connected:
                print("***Database Connected***")
        except Exception as e:
            print("Database not connected...")
    def close(self):
        self.connection.close()
    
    