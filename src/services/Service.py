class Service:
    """
    Abstraction for newcos-services
    """
    def __init__(self, name, url, port, endpoint):
        self.name = name
        self.url = url
        self.port = port
        self.endpoint = endpoint

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_port(self):
        return self.port

    def get_endpoint(self):
        return self.endpoint

    def get_service(self):
        """
        Build url to poll this service
        """
        return {self.name: '{}:{}{}'.format(self.url, self.port, self.endpoint)}