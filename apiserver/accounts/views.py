from django.http.response import HttpResponse


def authenticate(request):
    if request.method.lower() != 'post':
        return HttpResponse(status=405)

    username = request.POST.get('username') or ''
    password = request.POST.get('password') or ''

    if not username or not password:
        return HttpResponse('invalid payload', status=400)
    return HttpResponse('hello world')
