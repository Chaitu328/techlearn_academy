from django.shortcuts import render,redirect,get_object_or_404
from academy.models import Course,Trainer,Student
from .forms import CourseForm,TrainerForm,StudentForm
from .models import Course,Trainer,Student
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


def edit_course(request,id):
    course = get_object_or_404(Course,id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            print(form.errors)
    else:
        form = CourseForm(instance=course)
    context = {
        'form' : form,
        'Title' : 'Course',
        'action_url' : 'edit_course',
        'obj': course,
    }
    return render(request,'edit.html',context)

def edit_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer')
        else:
            print(form.errors)
    else:
        form = TrainerForm(instance=trainer)
    context = {
        'form' : form,
        'Title' : 'Trainer',
        'action_url' : 'edit_trainer',
        'obj': trainer,
    }
    return render(request,'edit.html',context)

def edit_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=student)
    context = {
        'form' : form,
        'Title' : 'Student',
        'action_url' : 'edit_student',
        'obj': student,
    }
    return render(request,'edit.html',context)