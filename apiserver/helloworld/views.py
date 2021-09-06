from django.http.response import HttpResponse


def hello_world(request):
    return HttpResponse('hello world')
