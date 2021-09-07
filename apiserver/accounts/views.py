from django.http.response import HttpResponse, JsonResponse

from . import models


def authenticate(request):
    if request.method.lower() != 'post':
        return HttpResponse(status=405)

    username = request.POST.get('username') or ''
    password = request.POST.get('password') or ''

    if not username or not password:
        return HttpResponse('invalid payload', status=400)

    user = models.User.find_by_credentials(username, password)
    if not user:
        return HttpResponse('mismatch credentials', status=401)

    token = models.AccessToken.create(user)
    return JsonResponse({'access_token': token.key}, status=201)
