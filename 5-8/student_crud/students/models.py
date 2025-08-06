from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gpa = models.FloatField()

    def __str__(self):
        return self.name