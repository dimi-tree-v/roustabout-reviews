from releases import views

from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('artists', views.ArtistViewSet)

urlpatterns = [
    path('', include(router.urls))
]
