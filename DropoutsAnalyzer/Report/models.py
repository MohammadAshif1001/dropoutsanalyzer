from django.db import models


class School(models.Model):

    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    caste = models.CharField(max_length=20, choices=[('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('OBC', 'Other Backward Class'), ('GEN', 'General')])
    age = models.IntegerField()
    standard = models.IntegerField()

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name


class Dropout(models.Model):
    reason = models.TextField()
    date = models.DateField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='dropout')

    def __str__(self):
        return self.reason
