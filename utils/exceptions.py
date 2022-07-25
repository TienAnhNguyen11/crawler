class ServiceException(Exception):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail


class NotAuthenticatedException(Exception):
    pass
