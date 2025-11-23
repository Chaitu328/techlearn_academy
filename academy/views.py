from django.shortcuts import render
from academy.models import Course,Trainer,Student
# Create your views here.
def course(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
    }
    return render(request, 'course.html',context)

def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers' : trainers,
    }
    return render(request, 'trainer.html',context)

def student(request):
    students = Student.objects.all()
    context = {
        'students' : students,
    }
    return render(request, 'student.html',context)