import mysql.connector as sql
import util.PropertyUtil as PropertyUtil
class DBConnection:
    def open(self):
        try:
            conn=PropertyUtil.getPropertyString()
            self.connection=sql.connect(host=conn[1],database=conn[2],username=conn[0],password=conn[3])
            self.stmt=self.connection.cursor()
            if self.connection.is_connected:
                print("***Database Connected***")
        except Exception as e:
            print("Database not connected...")
    def close(self):
        self.connection.close()
    
    