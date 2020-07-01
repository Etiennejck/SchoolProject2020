from rest_framework import serializers
from School_Models import models

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SchoolPg
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Meal
        fields = '__all__'

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class RulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Rules
        fields = '__all__'

class School_yearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.School_year
        fields = '__all__'

class InscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Inscription
        fields = '__all__'

class School_SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.School_Section
        fields = '__all__'

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class Room_TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Room_Type
        fields = '__all__'

class Class_room_StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Class_room_Student
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Grade
        fields = '__all__'

class LeaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Leave
        fields = '__all__'

class Leave_CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Leave_Categorie
        fields = '__all__'

class Professor_ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Professor_Report
        fields = '__all__'

class Professor_CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Professor_Course
        fields = '__all__'

class CommunicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Communication
        fields = '__all__'

class ClassDiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ClassDiary
        fields = '__all__'

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Level
        fields = '__all__'

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Section
        fields = '__all__'

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Parent
        fields = '__all__'

class Parent_StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Parent_Student
        fields = '__all__'

class Family_TieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Family_Tie
        fields = '__all__'

class AbsenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Absence
        fields = '__all__'
