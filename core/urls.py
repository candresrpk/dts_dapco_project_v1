from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('my_apps.users.urls')),
    path('', include('my_apps.dapco.urls')),
    path('users/', include('my_apps.users.urls')),
    
]