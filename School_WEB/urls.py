from django.conf.urls import url
from django.urls import path
from School_WEB import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^dashboardParent/', views.dashboardParent, name='dashboardParent'),

    ]