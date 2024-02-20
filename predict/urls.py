from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("upload/", views.upload),
    path("error/", views.error),
    path("complete/", views.complete),
    path("logo/", views.logo),

]