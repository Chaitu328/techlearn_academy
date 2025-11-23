from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    duration = models.PositiveIntegerField()
    course_image = models.ImageField(upload_to='images',default="course1.png")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name
    
class Trainer(models.Model):
    expertise_choice = [
    ("python", "Python"),
    ("django", "Django"),
    ("data_science", "Data Science"),
    ]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=100, choices=expertise_choice)
    trainer_photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True, blank=True)
    trainer = models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'