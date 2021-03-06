from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import HelloAPIView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)


app_name = 'profile_api'

urlpatterns = [
    path('hello-view', HelloAPIView.as_view(), name="helloApi"),
    path('', include(router.urls))

]
