class PortInfo:

    def __init__(self, privatePort, publicPort):
        self.privatePort = privatePort
        self.publicPort = publicPort

    def __str__(self):
        result = "{}->{}".format(self.publicPort, self.privatePort)
        return result