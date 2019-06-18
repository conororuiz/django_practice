from django.core.cache import cache

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        count = cache.get(request.META.get('PATH_INFO')) or 0
        count += 1
        cache.set(request.META.get('PATH_INFO'), count)
        response = self.get_response(request)
        return response