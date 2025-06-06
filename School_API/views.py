from django.shortcuts import render
from rest_framework import viewsets
from School_Models.models import *
from School_API.serializers import *

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = SchoolPg.objects.all()
    serializer_class = SchoolSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class RulesViewSet(viewsets.ModelViewSet):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer

class SchoolYearViewSet(viewsets.ModelViewSet):
    queryset = School_year.objects.all()
    serializer_class = School_yearSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

class SchoolSectionViewSet(viewsets.ModelViewSet):
    queryset = School_Section.objects.all()
    serializer_class = School_SectionSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ClassRoomStudentViewSet(viewsets.ModelViewSet):
    queryset = Class_room_Student.objects.all()
    serializer_class = Class_room_StudentSerializer

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = Room_Type.objects.all()
    serializer_class = Room_TypeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class Leave_CategorieViewSet(viewsets.ModelViewSet):
    queryset = Leave_Categorie.objects.all()
    serializer_class = Leave_CategorieSerializer

class Professor_ReportViewSet(viewsets.ModelViewSet):
    queryset = Professor_Report.objects.all()
    serializer_class = Professor_ReportSerializer

class Professor_CourseViewSet(viewsets.ModelViewSet):
    queryset = Professor_Course.objects.all()
    serializer_class = Professor_CourseSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

class ClassDiaryViewSet(viewsets.ModelViewSet):
    queryset = ClassDiary.objects.all()
    serializer_class = ClassDiarySerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class =  ReportSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class =  SectionSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class Parent_StudentViewSet(viewsets.ModelViewSet):
    queryset = Parent_Student.objects.all()
    serializer_class = Parent_StudentSerializer

class Family_TieViewSet(viewsets.ModelViewSet):
    queryset = Family_Tie.objects.all()
    serializer_class = Family_TieSerializer

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer

class MessageSendViewSet(viewsets.ModelViewSet):
    queryset = MessageSend.objects.all()
    serializer_class = MessageSendSerializer


def index(request):
    return render(request, "base.html")

# def updateJdc(user, message):
#     Student.objects.filter(parents_id__mail=user.email).update(class_journal=message)

def getStudentList(classId=None):
    """Return a student or the full student list."""
    if classId:  # filtrage des étudiants par id
        return Student.objects.get(id=classId)
    else:
        return Student.objects.all()

def getChildren(parentEmail):
    """Return children for a given parent."""
    return Student.objects.filter(id_parent_id=parentEmail)

def getStudentById(id):
    """Return a student identified by its id."""
    return Student.objects.get(id=id)

def setStudentAttendee(id):
    """Toggle presence flag for a student."""
    Student.objects.filter(pk=id).update(presence=not Student.objects.get(pk=id).presence)

def getJDCList(jdcId=None):
    """Return class diaries or one diary if an id is provided."""
    if jdcId:
        return ClassDiary.objects.get(id=jdcId)
    else:
        return ClassDiary.objects.all()

def getCommunication(studId=None):
    """Return communications or one if an id is provided."""
    if studId:
        return Communication.objects.get(id=studId)
    else:
        return Communication.objects.all()

def getAbsence(AbsencestudId=None):
    """Return absences or one absence for the provided id."""
    if AbsencestudId:
        return Absence.objects.get(id=AbsencestudId)
    else:
        return Absence.objects.all()


def getParentList(classId=None):
    """Return parents or one parent if an id is provided."""
    if classId:  # filtrage des étudiants par id
        return Parent.objects.get(id=classId)
    else:
        return Parent.objects.all()

def getProfessor(classId=None):
    """Return employees or one employee if an id is provided."""
    if classId:  # filtrage des étudiants par id
        return Employee.objects.get(id=classId)
    else:
        return Employee.objects.all()


def getEvents(classId=None):
    """Return events or one event if an id is provided."""
    if classId:  # filtrage des étudiants par id
        return Event.objects.get(id=classId)
    else:
        return Event.objects.all()

def getMessageSend(MessageSendId=None):
    """Return messages or one message if an id is provided."""
    if MessageSendId:  # filtrage des étudiants par id
        return MessageSend.objects.get(id=MessageSendId)
    else:
        return MessageSend.objects.all()

def getMenu(MenuId=None):
    """Return menus or one menu if an id is provided."""
    if MenuId:  # filtrage des étudiants par id
        return Menu.objects.get(id=MenuId)
    else:
        return Menu.objects.all()
