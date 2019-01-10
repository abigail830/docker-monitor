from dockermon.PortInfo import PortInfo


class ContainerInfo:
    names = []
    status = 'Nil'
    ports = []

    def __init__(self, container):

        if 'Names' in container.keys():
            for name in container['Names']:
                self.names.append(name)

        if 'State' in container.keys():
            self.state = container['State']

        if 'Ports' in container.keys():
            for port in container['Ports']:
                port_info = PortInfo(port)
                self.ports.append(port_info)

    def __str__(self):
        result = "Docker {} is {} with Ports {} ".format(self.name, self.state, self.ports)
        return result
