from django.shortcuts import render
from academy.models import Course, Trainer,Student

def home(request):
    total_courses = Course.objects.all().count()
    total_trainers =  Trainer.objects.all().count()
    total_students = Student.objects.all().count()
    context = {
        'total_courses' : total_courses,
        'total_trainers' : total_trainers,
        'total_students' : total_students,
    }
    return render(request, 'home.html', context)