from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Car(models.Model):
    Car_name = models.CharField('Марка', max_length=200)
    Man_date = models.DateTimeField('Дата производства')
    def __str__(self):
        return self.Car_name

class Driver(models.Model):
    First_name = models.CharField('Имя', max_length=30)
    Last_name = models.CharField('Фамилия', max_length=30)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return self.First_name +' '+self.Last_name
