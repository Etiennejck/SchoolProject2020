from django.conf.urls import url

from School_WEB import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboardParent/', views.dashboardParent, name='dashboardParent'),
    url(r'^dashboardProfessor/', views.dashboardProfessor, name='dashboardProfessor'),
    url(r'^dashboardDirection/', views.dashboardDirection, name='dashboardDirection'),
    url(r'^JournalDeClasse/', views.JournalDeClasse, name='JournalDeClasse'),
    url(r'^LogOut_view/', views.LogOut_view, name='LogOut_view'),
    url(r'^homeSchool/', views.homeSchool, name='homeSchool'),
    url(r'^contactUs/', views.contactUs, name='contactUs'),
    url(r'^logindpp/', views.logindpp, name='logindpp'),
    url(r'^detailJournalDeClasse/(\d+)/', views.detailJournalDeClasse, name='detailJournalDeClasse'),
    url(r'^updateJournaDeClasse/(\d+)/', views.updateJournaDeClasse, name='updateJournaDeClasse'),
    url(r'^deleteJournaDeClasse/(\d+)/', views.deleteJournaDeClasse, name='deleteJournaDeClasse'),
    url(r'inscriptionParent/', views.inscriptionParent, name='inscriptionParent'),
    url(r'inscriptionStudent/', views.inscriptionStudent, name='inscriptionStudent'),
    ]