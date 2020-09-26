from django.db import models
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField


class SchoolPg(models.Model):
    name = models.CharField(max_length=100)
    years = models.IntegerField()
    street = models.CharField(max_length=200)
    town = models.CharField(max_length=50)
    cp = models.IntegerField()
    matricul = models.IntegerField()
    status = models.BooleanField()
    def __str__(self):
        return "{}".format(self.name)

class Event(models.Model):
    name = models.CharField(max_length=100)
    periode = models.CharField(max_length=50)
    start_Date = models.DateField()
    end_Date = models.DateField()
    status = models.BooleanField()
    contry = models.CharField(max_length=100)
    Eventmessage = models.TextField(null=True)
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE, null=True)#Attention
    def __str__(self):
        return "{}, période: {} ".format(self.name, self.periode)

class Meal(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    id_menu = models.ForeignKey('Menu', on_delete=models.CASCADE)



class Menu(models.Model):
    name = models.CharField(max_length=100)
    starter = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

class MealMenu(models.Model):
    id_menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    id_meal = models.ForeignKey('Meal', on_delete=models.CASCADE)

class Rules(models.Model):
    name = models.CharField(max_length=100)
    years = models.IntegerField()
    text = models.TextField()
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE, null=True)#Attention

class School_year(models.Model):
    libel = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class Inscription(models.Model):
    date_inscription = models.DateField(auto_now=True)
    id_School_year = models.ForeignKey('School_year', on_delete=models.CASCADE)
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE, null=True)#Attention changer null
    def __str__(self):
        return str(self.id_School_year.start_date)

class School_Section(models.Model):
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE)
    id_section = models.ForeignKey('Section', on_delete=models.CASCADE)

#ClassRoom_Model

class Room(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    place_number = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    id_room_type = models.ForeignKey('Room_Type', on_delete=models.CASCADE)

class Room_Type(models.Model):
    name = models.CharField(max_length=50, null=True)#Attention
    dateNow = models.DateField()

class Class_room_Student(models.Model):
    id_classroom = models.ForeignKey('Room', on_delete=models.CASCADE)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_professor = models.ForeignKey('Employee', on_delete=models.CASCADE)

#Employee_Model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthday = models.DateField()
    mail = models.EmailField()
    phone_number = PhoneNumberField(null=True, region='BE')
    dateInscription = models.DateField()
    actif = models.BooleanField(default=True)
    id_grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE)
    id_section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return '{}, {} {}'.format(self.name, self.firstname, self.id_section)


class Grade(models.Model):
    designation = models.CharField(max_length=50)
    def __str__(self):
        return self.designation

class Leave(models.Model):
    intituled = models.CharField(max_length=150)
    start_day = models.DateField()
    end_day = models.DateField()
    document = models.FileField()
    id_leave_cat = models.ForeignKey('Leave_Categorie', on_delete=models.CASCADE)
    id_professor = models.ForeignKey('Employee', on_delete=models.CASCADE)

class Leave_Categorie(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title


class Professor_Report(models.Model):
    id_employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    id_report = models.ForeignKey('Report', on_delete=models.CASCADE)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_School_year = models.ForeignKey('School_year',on_delete=models.CASCADE)

class Professor_Course(models.Model):
    id_professor = models.ForeignKey('Employee', on_delete=models.CASCADE)
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.id_professor.name, self.id_course.name)


#Diary

class MessageSend(models.Model):
    id_parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    id_professor = models.ForeignKey('Employee', on_delete=models.CASCADE)
    messagesBody = models.TextField()
    msg_time = models.DateTimeField(auto_now=True)

class Communication(models.Model):
    id_employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    id_classdiary = models.ForeignKey('ClassDiary', on_delete=models.CASCADE, verbose_name="Journal de classe de ")
    comportement = models.TextField()
    home_work = models.TextField()
    communication = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return "{} Devoirs: {}, Notes de comportements: {}".format(self.id_classdiary.id_student.name, self.home_work, self.comportement)

class ClassDiary(models.Model):
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_level = models.ForeignKey('Level', on_delete=models.CASCADE)
    id_Schoolyear = models.ForeignKey('School_year', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_student)


class Level(models.Model):
    level = models.IntegerField()
    id_School_year = models.ForeignKey('School_year', on_delete=models.CASCADE)
    id_inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE)
    id_section = models.ForeignKey('Section', on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.level, self.id_section.name)

class Report(models.Model):
    trimestrial = models.IntegerField()
    id_level = models.ForeignKey('Level', on_delete=models.CASCADE)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=50)
    section_year = models.IntegerField()
    trimestrial = models.IntegerField()
    def __str__(self):
        return "{} {}".format(self.name, self.section_year)

class Course(models.Model):
    name = models.CharField(max_length=150)
    ponderation = models.DecimalField(max_digits=5, decimal_places=2)
    id_section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

#Student_Models

class Student(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.CharField(max_length=3)
    nationality = models.CharField(max_length=70)
    mother_tong = models.CharField(max_length=50)
    hot_meal = models.BooleanField(default=False)
    output_School = models.BooleanField(default=False)
    agreement_image = models.BooleanField(default=False)
    educational_agreement = models.BooleanField(default=False)
    presence = models.BooleanField(default=False)
    image = models.ImageField(null=True)
    id_parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    id_School = models.ForeignKey('SchoolPg', on_delete=models.CASCADE)
    id_level = models.ForeignKey('Level', on_delete=models.CASCADE)
    id_inscription = models.ForeignKey('Inscription', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.name, self.first_name, self.id_parent.email)


class Parent(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=70)
    mother_tong = models.CharField(max_length=50)
    street_number = models.CharField(max_length=100)
    ZIP_code = models.IntegerField()
    city = models.CharField(max_length=80)
    email = models.EmailField()
    Telephone = PhoneNumberField(null=True, region='BE')
    dateInscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.first_name, self.email)

class Parent_Student(models.Model):
    id_parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    id_family_tie = models.ForeignKey('Family_Tie', on_delete=models.CASCADE)

class Family_Tie(models.Model):
    Designation = models.CharField(max_length=150)
    def __str__(self):
        return self.Designation

class Absence(models.Model):
    document = models.FileField()
    start_date = models.DateField()
    end_date = models.DateField()
    messageAbs = models.TextField(null=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    def __str__(self):
        return self.id_student.name



