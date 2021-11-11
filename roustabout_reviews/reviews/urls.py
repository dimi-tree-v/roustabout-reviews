from reviews import views

from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('articles', views.ArticleReviewViewset)
router.register('user-reviews', views.UserReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]
