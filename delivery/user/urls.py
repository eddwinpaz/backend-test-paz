from django.urls import path
from user.delivery.http.handler import getAll, getById
from user.delivery.http.handler import authentication, logout
from user.delivery.http.handler import create

urlpatterns = [
    path('', getAll),
    path('<str:userId>', getById),
    path('login/', authentication),
    path('create/', create),
    path('logout/', logout),
]
