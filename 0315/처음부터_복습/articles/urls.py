
from django.contrib import admin
from django.urls import path 
from articles import views

urlpatterns = [
    path("create/", views.create),
    path("read/", views.read),
    path("read/<int:id>/",views.read_id),
    path("", views.article_list),
    path("<int:id>/", views.article_detail)
]
