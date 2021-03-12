from releases import views

from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('artists', views.ArtistViewSet)
router.register('members', views.MemberViewSet)
router.register('releases', views.ReleaseViewSet)
router.register('genres', views.GenreViewSet)
router.register('tracks', views.TrackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
