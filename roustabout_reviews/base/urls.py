from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from base.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('releases.urls'))
]
