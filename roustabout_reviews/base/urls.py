from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from base.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('releases.urls')),
    path('api/v1/', include('reviews.urls'))
]
