"""Serializers used by the School_API app."""

from rest_framework import serializers
from School_Models import models


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    """Base serializer configuring common behaviour."""

    class Meta:
        fields = "__all__"

class SchoolSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.SchoolPg

class EventSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Event

class MealSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Meal

class MenuSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Menu

class RulesSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Rules

class School_yearSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.School_year

class InscriptionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Inscription

class School_SectionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.School_Section

class RoomSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Room

class Room_TypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Room_Type

class Class_room_StudentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Class_room_Student

class EmployeeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Employee

class GradeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Grade

class LeaveSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Leave

class Leave_CategorieSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Leave_Categorie

class Professor_ReportSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Professor_Report

class Professor_CourseSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Professor_Course

class CommunicationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Communication

class ClassDiarySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.ClassDiary

class LevelSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Level

class ReportSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Report

class SectionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Section

class CourseSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Course

class StudentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Student

class ParentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Parent

class Parent_StudentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Parent_Student

class Family_TieSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Family_Tie

class AbsenceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.Absence

class MessageSendSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = models.MessageSend
