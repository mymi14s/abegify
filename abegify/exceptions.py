

from django.http import JsonResponse

class JsonHttpException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

def http_exception(status_code, message):
    raise JsonHttpException(status_code, message)
