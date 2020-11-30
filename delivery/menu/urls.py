from django.urls import path
from menu.delivery.http.handler import getAll, getById, getTodayMenu
from menu.delivery.http.handler import addMenu, deleteMenu, updateMenu
from menu.delivery.http.handler import broadcast_whatsapp_menu

urlpatterns = [
    path('', getAll),
    path('<str:menuId>', getById),
    path('today/', getTodayMenu),
    path('add/', addMenu),
    path('broadcast-whatsapp-menu/', broadcast_whatsapp_menu),
    path('delete/<str:menuId>', deleteMenu),
    path('update/<str:menuId>', updateMenu),
]
