from django.http import JsonResponse
from .exceptions import JsonHttpException 

class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except JsonHttpException as e:
            return JsonResponse({'error': e.message}, status=e.status_code)
