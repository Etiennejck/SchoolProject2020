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
    serializer_class = MenuSerializer

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


def index(request):
    return render(request, "base.html")

# def updateJdc(user, message):
# #     Student.objects.filter(parents_id__mail=user.email).update(class_journal=message)

# def getStudentList(classId=None):
#     if classId:#filtrage des étudiants par id
#         return ["Eliott", "Eleonor", "Emile", "Aubane"]
#     else:
#         return ["Eliott", "Eleonor", "Emile", "Aubane", "Ferra", "Lucie", "Charles", "Basile", "Nathan"]