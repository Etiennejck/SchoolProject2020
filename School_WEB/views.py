from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_protect
from School_Models.models import Student, Parent,Employee, Communication, Section
from django.contrib import messages
from requests.auth import HTTPBasicAuth
from School_WEB import chat
import requests, json
from School_API import views
from .forms import CommunicationForm, InscriptionParentForm, InscriptionStudentForm, AbsenceForm, addAbsenceForm, MessageSendForm
from School_WEB.chat import *

def inscriptionParent(request):
    context = {}
    form = InscriptionParentForm(request.POST or None)
    if form.is_valid():
        password = request.POST['pass']
        User.objects.create_user(username=form.cleaned_data['name'], password=password,
                                 email=form.cleaned_data['email'])
        request.session['comeIn'] = form.cleaned_data['email']
        form.save()
        return redirect('inscriptionStudent')
    context['form'] = form
    return render(request, 'web/inscriptionParent.html', context)


def inscriptionStudent(request):
    #parent = get_object_or_404(Parent, id=id)
    context = {}
    parent = [p.id for p in views.getParentList() if p.email == request.session.get('comeIn')]
    form = InscriptionStudentForm(request.POST or None, initial={'id_parent':parent})
    if form.is_valid():
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
        s_id = [s.id for s in views.getStudentList() if s.id_parent.email == user.email]
        sudent = [st for st in views.getStudentList() if st.id_parent.email == user.email]
        jdc = [stJ for stJ in views.getCommunication() if stJ.id_classdiary.id_student.id_parent.email == user.email]
        prof = [prof for prof in views.getProfessor() if views.getStudentList(str(s_id[0])).id_level.id_section == prof.id_section]
        chatMessage = [m for m in views.getMessageSend() if m.id_parent.email == user.email]
        events = [e for e in views.getEvents().order_by('start_Date') if e.status == True]
        heureEnvoi = datetime.datetime.now()
        url = 'http://0.0.0.0:8000/apiabsence/'
        if request.method == 'POST':
            data = views.getAbsence()
            data.get_or_create(document=request.POST['document'],
                start_date=request.POST['startdate'],
                end_date=request.POST['enddate'],
                messageAbs=request.POST['message'],
                id_student_id=s_id[0]
                )

        s = requests.get('http://0.0.0.0:8000/apiabsence/')
        context = {
            'user': user,
            'heureEnvoi': heureEnvoi,
            'sudent': sudent,
            'jdc': jdc,
            's_id': s_id[0],
            'prof': prof,
            'events': events,
            'eventslen': len(events),
            'chatMessage': chatMessage,
            'menu': views.getMenu()

        }
        print(user.email, user.id, s_id, s.text, s.url)
        return render(request, 'web/dashboardParent.html',context)
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')


# Profesor--------------------------------------------------------------------
@csrf_protect
def dashboardProfessor(request):
    if request.user.is_authenticated and request.user.is_staff:
        user = request.user
        connection = datetime.datetime.now()
        profList = [pl.id for pl in views.getProfessor() if pl.mail == user.email]
        profList_section = [pl.id_section for pl in views.getProfessor() if pl.mail == user.email]
        studentList = [s for s in views.getStudentList() if s.id_level.id_section == profList_section[0]]
        studentPresent = [sp for sp in studentList if sp.presence == True]
        JDCList = [a for a in views.getCommunication().filter(date=connection) if a.id_employee.id_section == profList_section[0]]
        StudentabsenceList = [a for a in views.getAbsence() if a.id_student.id_level.id_section == profList_section[0] and a.end_date >= connection.date()]
        chatMessage = [m for m in views.getMessageSend() if m.id_professor.mail == user.email]
        print(profList_section, profList[0])
        request.session["user"] = user.email
        form = CommunicationForm(request.POST or None, initial={'id_employee': profList })
        if form.is_valid():
            form.save()
            return redirect('dashboardProfessor')

        if request.method == 'POST':
            comGen = request.POST['comGen']
            Id_student = request.POST['id']
            views.setStudentAttendee(Id_student)
            views.getCommunication().filter(id_employee__id_section=profList_section[0]).update(communication=comGen)
            return redirect('dashboardProfessor')

        contentList = {
            'user': user,
            'connection': connection,
            "students": studentList,
            'NbrStud':len(studentList),
            "JDCList": JDCList,
            'NbrAbs': len(StudentabsenceList),
            "StudentabsenceList":StudentabsenceList,
            'eventsList': views.getEvents(),
            'form': form,
            'chatMessage':chatMessage,
            'chatMessageLen': len(chatMessage),
            'proflist': profList[0],
            'studentPresent': len(studentPresent),
            'menu':views.getMenu()
        }
        print(user.email, user.id, connection)
        return render(request, 'web/dashboardProfessor.html', contentList)
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')

def communication(request):
    context = {}
    section = Section.objects.all()

    context['JDCMaternelleOne'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=5)
    context['JDCMaternelleTwo'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=6)
    context['JDCMaternelleTrhee'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=7)
    context['JDCPrimaireOne'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=1)
    context['JDCPrimaireTwo'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=2)
    context['JDCPrimaireTrhee'] = views.getCommunication().filter(id_classdiary__id_level__id_section_id=3)
    context['JDCList'] = views.getCommunication()

    return render(request, 'web/communication.html', context)

def messagesend(request, idStu):
    if request.user.is_authenticated and request.user.is_staff or request.user.groups.exists():
        sId = get_object_or_404(Student,id=idStu)
        context = {}
        user = request.user
        profId = [p.id for p in views.getProfessor() if p.mail == request.session.get('user')]
        parentId = [pnt.id for pnt in views.getParentList()]
        messageReciep = [m for m in views.getMessageSend()]
        form = MessageSendForm(request.POST or None, initial={'id_professor': profId, 'id_parent': sId.id_parent})
        if request.method == 'POST':
            if form.is_valid():
                form.save()

        context['form'] = form
        context['profId'] =profId
        context['parentId'] = parentId
        context['messageReciep'] = messageReciep
        context['user'] = user
        context['user_email'] = request.session.get('user')
        context['sId'] = sId

        return render(request, 'web/chat.html', context)
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')

def JournalDeClasse(request, id):
    studentJDC = get_object_or_404(Communication, id=id)
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
        'form': form,
        'studentJDC': studentJDC
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


def addAbsenceStudent(request):
    context = {}
    printDate = datetime.datetime.now()
    Date = printDate.strftime('%x')
    form = AbsenceForm(request.POST or None, initial={'id_student':request.session.get('parent')})
    if form.is_valid():
        form.save()
        return redirect('dashboardParent')

    context['form'] = form
    return render(request, 'web/addAbsenceStudent.html', context)

def DetailsAbsenceStudent(request):
    context = {}
    abs = [a for a in views.getAbsence()]
    context['absenceList'] = abs

    return render(request, 'web/DetailsAbsenceStudent.html', context)



def dashboardDirection(request):
    if request.user.is_authenticated and request.user.is_staff:
        context = {}
        user = request.user

        connection = datetime.datetime.now()
        avgSchool = views.getStudentList()
        context['user'] = user
        context['avgSchool'] = int(len(avgSchool)*100/300)
        context['chatMessageLen'] = views.getMessageSend()
        context['studentList'] = views.getStudentList()
        context['absenceList'] = views.getAbsence()
        context['eventsList'] = views.getEvents()
        context['JDCList'] = views.getCommunication()
        context['menu'] = views.getMenu()
        return render(request, 'web/dashboardDirection.html', context)
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('home')

def LogOut_view(request):
    logout(request)
    return render(request, 'web/home.html')


def homeSchool(request):
    return render(request, 'web/homeSchool.html')


def contactUs(request):
    return render(request, 'web/contactUs.html')


def logindpp(request):
    return render(request, 'web/logindpp.html')


def echat(request):

    return render(request, 'web/chat.html')