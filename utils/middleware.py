from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User


class LoginStatusMiddleware(MiddlewareMixin):
    def process_request(self, request):
            if request.path in ['/backweb/login/', '/backweb/register/', '/web/index/']:
                return None
            user_id = request.session.get('user_id')
            if user_id:
                request.user = User.objects.get(pk=user_id)
                return None
            else:
                return HttpResponseRedirect('/backweb/login/')

    def process_response(self, request, response):

        return response
