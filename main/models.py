from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
) 

# Create your models here.


class Teacher(models.Model):
    t_name = models.CharField(max_length=256)
    t_id = models.IntegerField()
    subject = models.CharField(max_length=100)
    gender = models.BooleanField()

    def __str__(self):
        return self.t_name

class Course(models.Model):
    c_name = models.CharField(max_length=100)
    c_id = models.CharField
    teacher = models.ForeignKey('Teacher' , on_delete = models.CASCADE)

        def __str__(self):
            return self.c_name

class Student(models.Model):
    s_name = models.CharField(max_length = 256)
    roll_no = models.IntegerField(validators=[
                MinValueValidator(0)] )
    s_id = models.IntegerField()
    course = models.ManyToManyField('Course')   # Many students can have many courses

    def __str__(self):
        return self.name