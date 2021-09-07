from django.urls import path

from . import views

urlpatterns = [
    path('auth/', views.authenticate),
    path('me/', views.user_info),
]
