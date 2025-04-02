from django.utils.deprecation import MiddlewareMixin

class DisableCSRFOnAPIMiddleware(MiddlewareMixin):
    """
    Disable CSRF protection for API endpoints only.
    """
    def process_request(self, request):
        if request.path.startswith('/apis/method/'):  # ✅ Adjust based on your API URL
            setattr(request, '_dont_enforce_csrf_checks', True)
