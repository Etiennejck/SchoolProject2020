from django.contrib import admin
from School_API.views import *
# Register your models here.

admin.site.register(SchoolPg)
admin.site.register(Event)
admin.site.register(Meal)
admin.site.register(Menu)
admin.site.register(MealMenu)
admin.site.register(Rules)
admin.site.register(Room)
admin.site.register(Class_room_Student)

admin.site.register(Employee)
admin.site.register(Professor_Course)
admin.site.register(Professor_Report)
admin.site.register(Report)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Section)


admin.site.register(Student)
admin.site.register(Level)
admin.site.register(Parent)
admin.site.register(ClassDiary)


admin.site.register(Leave)
admin.site.register(Leave_Categorie)
admin.site.register(Absence)

admin.site.register(Communication)