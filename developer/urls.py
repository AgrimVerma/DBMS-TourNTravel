from django.contrib import admin
from django.urls import path
from developer import views

urlpatterns = [
    path("admin_login", views.index),
    # path("/print", views.print)
]
