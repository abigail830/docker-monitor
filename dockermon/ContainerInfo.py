from dockermon.PortInfo import PortInfo

class ContainerInfo:

    def __init__(self, name, ports, status):
        self.name = name[name.index('/'):]
        self.status = status
        self.ports = []
        for port in ports:
            port_info = PortInfo(port['PrivatePort'], port['PublicPort'])
            self.ports.append(port_info)

    def __str__(self):
        result = "Docker {} with Ports {} is {}".format(self.name, self.ports, self.status)
        return result
