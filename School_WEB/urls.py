from django.conf.urls import url
from django.urls import path

from School_WEB import views

urlpatterns = [
    url(r'^', views.home, name='home'),

    ]