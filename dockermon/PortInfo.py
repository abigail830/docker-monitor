class PortInfo:

    privatePort = 'Nil'
    publicPort = 'Nil'

    def __init__(self, port):
        if 'PrivatePort' in port.keys():
            self.privatePort = port['PrivatePort']

        if 'PublicPort' in port.keys():
            self.publicPort = port['PublicPort']

    def __str__(self):
        result = "{}->{}".format(self.publicPort, self.privatePort)
        return result
