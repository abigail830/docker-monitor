from dockermon.PortInfo import PortInfo

class ContainerInfo:

    def __init__(self, name, ports, status):
        self.name = name
        self.status = status
        self.ports = ports
        for port in ports:
            port_info = PortInfo(port['PrivatePort'])
            self.ports.append(port_info)
            print("{}".format(port))

    def __str__(self):
        result = "Docker {} with Ports {} is {}".format(self.name, self.ports, self.status)
        return result
