
from django.conf.urls import url
from documentation import views

urlpatterns = [
    url(r'^upload', views.upload, name="upload"),
    url(r'^delete', views.delete, name="delete"),
    url(r'^moreInfo', views.moreInfo, name="moreInfo"),
    url(r'^', views.home, name="home"),
]
