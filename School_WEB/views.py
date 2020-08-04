from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from School_Models.models import Student, Parent
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardParent')
        else:
            messages.info(request, 'your email or password is not correct',)
            return redirect('home')

    return render(request, 'web/home.html')

def dashboardParent(request):
    if request.user.is_authenticated and request.user.groups.exists():
        user = request.user
        heureEnvoi = datetime.datetime.now()

        print(user.email, user.id)
        if request.method == 'POST':
            message = request.POST['message']
            Student.objects.filter(parents_id__mail=user.email).update(class_journal=message)

        return render(request, 'web/dashboardParent.html',
                      {'user': user, 'heureEnvoi': heureEnvoi.strftime('%X')})
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')


def dashboardProfessor(request):

    return render(request, 'web/dashboardProfessor.html')

def dashboardDirection(request):

    return render(request, 'web/dashboardDirection.html')

def JournalDeClasse(request):
    Stud = Student.objects.all()
    Pare = [p.name for p in Parent.objects.all()]


    printDate = datetime.datetime.now()
    studentJDC = {
        "Date": printDate.strftime('%x'),
        "Devoir": "Calcul mental",
        "Notes": "Etienne c'est bien comporter aujourd'hui"
    }
    contextList = {
        'liststudent': studentJDC,
        'parent': Pare,
        'student': Stud
    }

    return render(request, 'web/JournalDeClasse.html',contextList)

def LogOut_view(request):
    logout(request)
    return render(request, 'web/home.html')

def homeSchool(request):
    return render(request, 'web/homeSchool.html')