from django.http.response import HttpResponse


def authenticate(request):
    if request.method.lower() != 'post':
        return HttpResponse(status=405)

    return HttpResponse('hello world')
