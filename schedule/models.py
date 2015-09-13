from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    date = models.DateField()
    minutes = models.PositiveSmallIntegerField()
    project = models.ForeignKey(Project)
    content = models.TextField('Job Content', default='')
    
    def __str__(self):
        return self.date.strftime('%c') + ' works ' + str(self.minutes) + ' minutes'
