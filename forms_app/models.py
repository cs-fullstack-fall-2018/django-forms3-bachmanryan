from django.db import models
from datetime import datetime


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=500)
    timeCook = models.IntegerField()
    dateCreated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class NonProfitModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    establishedDate = models.DateTimeField(default=datetime.now)
    operatingBudget = models.IntegerField()
    NumOfEmployees = models.IntegerField()

    def __str__(self):
        return self.name
