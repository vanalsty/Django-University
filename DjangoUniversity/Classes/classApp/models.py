from django.db import models

class djangoClassesManager(models.Manager):
    pass

class djangoClasses(models.Model):
    courseNumber = models.IntegerField(primary_key='True')
    Title = models.CharField(max_length=50, default='', blank='True', null='False')
    Instructor = models.CharField(max_length=50, default='', blank='True', null='False')
    classDuration = models.FloatField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.Title
