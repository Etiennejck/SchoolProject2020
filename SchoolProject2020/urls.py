"""SchoolProject2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from School_API import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'schoolpg', views.SchoolViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'meal', views.MealViewSet)
router.register(r'menu', views.MenuViewSet)
router.register(r'rules', views.RulesViewSet)
router.register(r'schoolyear', views.SchoolYearViewSet)
router.register(r'inscription', views.InscriptionViewSet)
router.register(r'schoolSection', views.SchoolSectionViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'classRoomStudent', views.ClassRoomStudentViewSet)
router.register(r'roomType', views.RoomTypeViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'grade', views.GradeViewSet)
router.register(r'leave', views.LeaveViewSet)
router.register(r'leaveCategorie', views.Leave_CategorieViewSet)
router.register(r'professorReport', views.Professor_ReportViewSet)
router.register(r'professorCourse', views.Professor_CourseViewSet)
router.register(r'communication', views.CommunicationViewSet)
router.register(r'classDiary', views.ClassDiaryViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'report', views.ReportViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'parent', views.ParentViewSet)
router.register(r'parentStudent', views.Parent_StudentViewSet)
router.register(r'familyTie', views.Family_TieViewSet)
router.register(r'absence', views.AbsenceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
