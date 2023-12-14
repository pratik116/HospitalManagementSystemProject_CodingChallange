class doctorIdNotFound(Exception):
    def __init__(self): 
        super().__init__("Invalid Doctor Id")
