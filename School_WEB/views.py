from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_protect
from School_Models.models import Student, Parent
from django.contrib import messages
import requests, json
from School_API import views
from .forms import CommunicationForm, InscriptionParentForm, InscriptionStudentForm


def inscriptionParent(request):
    context = {}
    form = InscriptionParentForm(request.POST or None)
    if form.is_valid():
        password = request.POST['pass']
        User.objects.create_user(username=form.cleaned_data['name'], password=password,
                                 email=form.cleaned_data['email'])
        request.session['comeIn'] = form.cleaned_data['name']
        form.save()
        return redirect('inscriptionStudent')
    context['form'] = form
    return render(request, 'web/inscriptionParent.html', context)


def inscriptionStudent(request):
    # parent = get_object_or_404(Parent,id)
    context = {}
    form = InscriptionStudentForm(request.POST or None)
    if form.is_valid():
        form.fields['name'] = request.session.get("comeIn")
        form.save()
        return redirect('homeSchool')
    context['comeIn'] = request.session.get('comeIn')
    context['form'] = form
    return render(request, 'web/inscriptionStudent.html', context)


def home(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logindpp')
        else:
            messages.info(request, 'your email or password is not correct', )
            return redirect('home')

    return render(request, 'web/home.html')


# Parents-------------------------------------------------------------------------
def dashboardParent(request):
    if request.user.is_authenticated and request.user.groups.exists():
        user = request.user
        ugr = request.user.groups
        heureEnvoi = datetime.datetime.now()

        print(user.email, user.id)
        if request.method == 'POST':
            message = request.POST['message']
            Student.objects.filter(parents_id__mail=user.email).update(class_journal=message)

        return render(request, 'web/dashboardParent.html',
                      {'user': user, 'heureEnvoi': heureEnvoi.strftime('%X'), 'ugr': ugr})
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')


# Profesor--------------------------------------------------------------------
@csrf_protect
def dashboardProfessor(request):
    from School_API.views import viewsets
    if request.user.is_authenticated and request.user.is_staff:
        user = request.user
        connection = datetime.datetime.now()
        studentList = [s for s in views.getStudentList()]

        if request.method == 'POST':
            present = request.POST['present']
            presentStu = views.getStudentList(present)
            if not presentStu.presence:
                presentStu.presence = True
                presentStu.save()
            else:
                presentStu.presence = False
                presentStu.save()
            return redirect('dashboardProfessor')

        contentList = {
            'user': user,
            'connection': connection.today(),
            "students": studentList,

        }
        print(user.email, user.id, connection)
        return render(request, 'web/dashboardProfessor.html', contentList)
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')



def JournalDeClasse(request):
    printDate = datetime.datetime.now()
    Date = printDate.strftime('%x')
    JdcStud = [j for j in views.getCommunication().filter(date=printDate)]

    form = CommunicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('JournalDeClasse')
    Jdc = views.getCommunication()

    contextList = {
        "JdcStud": JdcStud,
        "Date": Date,
        "Jdc": Jdc,
        'form': form
    }
    return render(request, 'web/JournalDeClasse.html', contextList)


def detailJournalDeClasse(request, id):
    context = {}
    context["allJDC"] = [j for j in views.getCommunication().filter(id=id)]
    context["data"] = views.getCommunication().get(id=id)
    return render(request, 'web/detailJournalDeClasse.html', context)


def updateJournaDeClasse(request, id):
    context = {}
    obj = get_object_or_404(views.getCommunication(), id=id)
    form = CommunicationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('JournalDeClasse')

    context["form"] = form
    return render(request, 'web/updateJournaDeClasse.html', context)


def deleteJournaDeClasse(request, id):
    context = {}
    obj = get_object_or_404(views.getCommunication(), id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("JournalDeClasse")
    return render(request, 'web/deleteJournaDeClasse.html', context)


def dashboardDirection(request):
    return render(request, 'web/dashboardDirection.html')


def LogOut_view(request):
    logout(request)
    return render(request, 'web/home.html')


def homeSchool(request):
    return render(request, 'web/homeSchool.html')


def contactUs(request):
    return render(request, 'web/contactUs.html')


def logindpp(request):
    return render(request, 'web/logindpp.html')
