from django.urls import path
from accounts import views

urlpatterns = [
    path("register/", views.register),
    path("me/", views.me),
]

