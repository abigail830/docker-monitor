class PortInfo:

    def __init__(self, privatePort):
        self.privatePort = privatePort

    def __str__(self):
        result = "->{}".format(self.privatePort)
        return result
