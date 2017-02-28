
from django.conf.urls import url
from documentation import views

urlpatterns = [
    url(r'^network', views.network),
    url(r'^upload', views.upload),
    url(r'^delete', views.delete),
    url(r'^$', views.home),
]
