from django.urls import path
from . import views

app_name = "predict"
urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("prediction/", views.prediction, name="prediction")

   

]