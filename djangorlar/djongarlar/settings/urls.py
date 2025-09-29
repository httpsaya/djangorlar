from django.contrib import admin
from django.urls import path, include
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='hello'),
    path('users/', include('members.urls')),
    path('city-time/', include('timee.urls')),
    path('cnt/', include('count.urls'))
]
