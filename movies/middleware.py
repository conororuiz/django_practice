from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from movies.models import Token

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.META.get('PATH_INFO') not in ['/', reverse('logout')]:
            try:
               token=Token.objects.get(token=request.META.get('HTTP_AUTHENTICATION'))
               request.user=token.user
            except:
                    return redirect('login')
        response = self.get_response(request)

        return response

class ForceLogoutMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated() and request.user.force_logout_date and \
           request.session['LAST_LOGIN_DATE'] < request.user.force_logout_date:
            logout(request)