from django.http import HttpResponse
from django.views import View


def hello_world(request):
    return HttpResponse("hello word")


class helloindia(View):
    def get(self, request):
        return HttpResponse("hello india")