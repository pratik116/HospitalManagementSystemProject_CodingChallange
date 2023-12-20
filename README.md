# *Hospital Management System*
************************************************     


• The following Directory structure is to be followed in the application.


o entity
▪ Create entity classes in this package. All entity class should not have any
business logic.

o dao
▪ Create Service Provider interface to showcase functionalities.
▪ Create the implementation class for the above interface with db interaction.     


o exception
▪ Create user defined exceptions in this package and handle exceptions whenever
needed.     



o util
▪ Create a DBPropertyUtil class with a static function which takes property file
name as parameter and returns connection string.
▪ Create a DBConnUtil class which holds static method which takes connection
string as parameter file and returns connection object(Use method defined in
DBPropertyUtil class to get the connection String).     



o main
▪ Create a class MainModule and demonstrate the functionalities in a menu
driven application.     

### *To Run This Project:*        


> Go to the "DBPropertyUtil.py" file in the "UTIL" folder and change the host , user, password (and if needed the database name) as per your MySQL.     

> Finally go to the "main.py" file in the "MAIN" folder and run it. You are good to go.
