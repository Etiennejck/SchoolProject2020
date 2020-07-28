from django.shortcuts import render
import datetime

def home(request):

    return render(request, 'web/home.html')

def dashboardParent(request):

    return render(request, 'web/dashboardParent.html')

