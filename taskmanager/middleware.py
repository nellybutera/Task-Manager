from django.utils.cache import add_never_cache_headers

class NoCacheMiddleware:
    """
    Prevent browser caching for all authenticated pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            add_never_cache_headers(response)
        return response
