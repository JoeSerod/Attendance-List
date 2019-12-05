class Response:
    def __init__(self, data, status=200, error=""):
        self.status = status
        self.data = data
        self.error = error

    @staticmethod
    def new_error(error, status):
        return Response(None, status, error)

    @staticmethod
    def new_response(data):
        return Response(data)
