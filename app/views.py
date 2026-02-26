from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpRequest
from django.contrib import auth
from django.utils.translation import gettext as _

@api_view(['GET'])
def index_en(request: HttpRequest) -> Response:
    return Response(
        {
            'title': _('首页'),
            'message': _('您好，欢迎来到我的网站')
        }
    )

@api_view(['GET', 'POST'])
def sign_up(request: HttpRequest) -> Response:
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
