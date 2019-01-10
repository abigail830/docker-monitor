
class NoSuchContainerError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg
        print("No Container with 404")
        exit()


class ServerErrorError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg
        print("Internal server error with 500")

class BadParameterError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg
        print("Bad Parameter with 400")
        exit()