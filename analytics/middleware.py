from .models import Visit

class VisitTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # We don't want to log every request for static files or admin pages
        if request.path.startswith('/static/') or request.path.startswith('/admin/'):
            return self.get_response(request)

        # Create session if it doesn't exist
        if not request.session.session_key:
            request.session.create()

        visit = Visit(
            session_key=request.session.session_key,
            ip_address=self.get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            method=request.method,
            path=request.path,
            referrer=request.META.get('HTTP_REFERER', ''),
        )
        
        # Get the response first
        response = self.get_response(request)
        
        # Now we have the status code, save the visit object
        visit.status_code = response.status_code
        visit.save()

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip