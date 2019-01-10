from dockermon.PortInfo import PortInfo
import json

class ContainerInfo:
    names = 'Nil'
    status = 'Nil'
    ports = []

    def __init__(self, container):

        if 'Names' in container.keys():
            self.names = container['Names']

        if 'State' in container.keys():
            self.state = container['State']

        tmps=[]
        if 'Ports' in container.keys():
            for port in container['Ports']:
                port_info = PortInfo(port)
                tmps.append(port_info)

        self.ports = json.dumps([port.__dict__ for port in tmps])

    def __str__(self):
        result = "Docker {} is {} with Ports {} ".format(self.name, self.state, self.ports)
        return result
