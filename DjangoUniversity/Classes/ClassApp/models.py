from django.db import models #imported django model

class djangoClasses(models.Model): # defined class and which will inherit from model up above
    CourseNum = models.IntegerField(max_length=10, primary_key=True)
    Title = models.CharField(max_length=60, default='', null=False) # can have max length of 60 characters, that will automatically start of empty but in database they have to save something
    Instructor = models.CharField(max_length=60, default='', null=False)
    Duration = models.FloatField(null=False)

    objects = models.Manager() #created object manager to grab information

    def __str__(self):
        return self.Title
