class InvalidIdException(Exception):
    def __init__(self): 
        super().__init__("Invalid Appointment Id")
    