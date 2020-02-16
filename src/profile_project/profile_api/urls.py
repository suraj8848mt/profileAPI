from django.urls import path

from .views import HelloAPIView

app_name = 'profile_api'

urlpatterns = [
    path('hello-view', HelloAPIView.as_view(), name="helloApi")

]
