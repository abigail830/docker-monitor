class ContainerInfo:

    def __init__(self, name, ports, status):
        self.name = name
        self.ports = ports
        self.status = status

    def __str__(self):
        result = "Docker {} with Ports {} is {}".format(self.name, self.ports, self.status)
        return result
