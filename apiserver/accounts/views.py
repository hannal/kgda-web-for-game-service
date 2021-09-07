from django.http.response import HttpResponse


def authenticate(request):
    return HttpResponse('hello world')
