# error with custom message
class MyErrorMessage(Exception):
    def __init__(self, message):
        super().__init__(message)