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


@admin.register(Employee)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("last_name__startswith", )
    list_display = ("name", "firstname","id_grade","actif","id_section")

admin.site.register(Professor_Course)
admin.site.register(Professor_Report)
admin.site.register(Report)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Section)


@admin.register(Student)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("first_name__startswith", )
    list_display = ("id_parent","name", "first_name","id_level","presence","sex","image")



admin.site.register(Level)
admin.site.register(Parent)
admin.site.register(ClassDiary)


admin.site.register(Leave)
admin.site.register(Leave_Categorie)
admin.site.register(Absence)

admin.site.register(Communication)