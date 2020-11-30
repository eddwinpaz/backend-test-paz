from django.urls import path
from order.delivery.http.handler import getAll, getById, getAllById
from order.delivery.http.handler import placeOrder

urlpatterns = [
    path('', getAll),
    path('view/<str:orderId>', getById),
    path('all/', getAllById),
    path('create/<str:menuId>', placeOrder),

]
