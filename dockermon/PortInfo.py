class PortInfo:

    privatePort = 'Nil'
    publicPort = 'Nil'

    def __init__(self, port):
        if hasattr(port, 'PrivatePort'):
            self.privatePort = port['PrivatePort']

        if hasattr(port, 'PublicPort'):
            self.publicPort = port['PublicPort']

    def __str__(self):
        result = "{}->{}".format(self.publicPort, self.privatePort)
        return result
