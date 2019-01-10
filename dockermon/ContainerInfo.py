class ContainerInfo:

    def __init__(self, name, ports):
        self.name = name
        self.ports = ports

    def convert(self, resp_json):

        for item in resp_json:
            self.name = item['Name']
            self.ports = item['Ports']