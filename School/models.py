from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    years = models.IntegerField()
    street = models.CharField(max_length=200)
    town = models.CharField(max_length=50)
    cp = models.IntegerField()
    matricule = models.IntegerField()
    status = models.BooleanField()
    id_event = models.ForeignKey('Event', on_delete=models.CASCADE)
    id_repas = models.ForeignKey('Food', on_delete=models.CASCADE)
    id_rules = models.ForeignKey('Rules', on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=100)
    periode = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.BooleanField()
    contry = models.CharField(max_length=100)

class Food(models.Model):
    date = models.DateField()
    id_menu = models.ForeignKey('Menu',on_delete=models.CASCADE)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    starter = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

class Rules(models.Model):
    name = models.CharField(max_length=100)
    years = models.IntegerField()
    text = models.TextField()