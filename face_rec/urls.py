from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import IdentificationView, RegistrationView

app_name = "face_rec"

router = routers.DefaultRouter()
router.register('registration', RegistrationView)

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^identification', IdentificationView.as_view())
]