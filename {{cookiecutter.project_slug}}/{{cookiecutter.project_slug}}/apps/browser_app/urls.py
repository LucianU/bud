from django.urls import path

from . import views

app_name = "browser_app"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
]
