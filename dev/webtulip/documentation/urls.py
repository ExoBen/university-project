
from django.conf.urls import url
from documentation import views

urlpatterns = [

    url(r'^network', views.network),
    url(r'^$', views.home),
]
