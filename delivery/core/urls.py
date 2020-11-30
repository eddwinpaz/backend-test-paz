from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('messages',),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('menu/', include('menu.urls')),
    path('order/', include('order.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
