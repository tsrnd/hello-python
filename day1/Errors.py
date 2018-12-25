class Errors:
    def __init__(self, message, statusCode):
        self.message = message
        self.statusCode = statusCode

    def displayError():
        print('Error message :', self.message)