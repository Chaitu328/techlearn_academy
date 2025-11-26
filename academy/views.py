from django.shortcuts import render,redirect
from academy.models import Course,Trainer,Student
from .forms import CourseForm,TrainerForm,StudentForm
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


def add_course(request):
    if request.method == 'POST':
        form =CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            print(form.errors)
    form = CourseForm()
    context = {
        'form' : form,
        'Title': "Course",
        'action_url': 'add_course',
    }
    return render(request,'add.html',context)

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainer')
        else:
            print(form.errors)
    form = TrainerForm()
    context = {
        'form' : form,
        'Title': 'Trainer',
        'action_url': 'add_trainer',
    }
    return render(request,'add.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            print(form.errors)
    form = StudentForm()
    context = {
        'form' : form,
        'Title': 'Student',
        'action_url' : 'add_student',
    }
    return render(request,'add.html', context)

