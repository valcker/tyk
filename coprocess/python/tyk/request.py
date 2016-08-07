class TykCoProcessRequest:
    def __init__(self, request):
        self.__dict__ = request
    def add_header(self, key, value):
        self.set_headers[key] = value
    def delete_header(self, key):
        self.delete_headers = self.delete_headers + (key,)
    def add_param(self, key, value):
        self.add_params[key] = value
    def delete_param(self, key):
        self.delete_params = self.delete_params + (key,)
    def get_header(self, key):
        if key in self.headers:
            return self.headers[key][0]
        else:
            return None
