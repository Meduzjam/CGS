from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


class UserProfile(models.Model):  

    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Чувак'),
        (FEMALE, 'Чувиха'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField('Место жительства',max_length=140)  
    gender = models.CharField('Пол',max_length=1,choices=GENDER,default=MALE)
    def __str__(self):
        return u'Profile of user: %s' % self.user.username

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
