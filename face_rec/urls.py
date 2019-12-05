from django.conf.urls import url

from .views import UsersView, IdentificationView

app_name = "face_rec"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url(r'^users/', UsersView.as_view()),
    url(r'^identificate', IdentificationView.as_view()),
]