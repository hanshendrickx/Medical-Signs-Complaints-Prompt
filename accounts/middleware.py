from django.shortcuts import redirect
from django.contrib.auth import logout
from django.utils import timezone


class GuestExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_temporary:
            if request.user.expires_at and request.user.expires_at <= timezone.now():
                logout(request)
                # Redirect to login with message
                from django.contrib import messages

                messages.error(request, "Your guest session has expired.")
                return redirect("login")
        return self.get_response(request)
