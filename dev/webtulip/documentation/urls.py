
from django.conf.urls import url
from documentation import views

urlpatterns = [
    url(r'^upload', views.upload),
    url(r'^delete', views.delete),
    url(r'^', views.home),
]
