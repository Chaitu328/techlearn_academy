from django.shortcuts import render,redirect,get_object_or_404
from academy.models import Course,Trainer,Student
from .forms import CourseForm,TrainerForm,StudentForm
from .models import Course,Trainer,Student
from django.contrib.auth.decorators import login_required,permission_required
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


# ---------------------ADD--------------------
@login_required
@permission_required('academy.add_course',raise_exception=True)
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


@login_required
@permission_required('academy.add_trainer',raise_exception=True)
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


@login_required
@permission_required('academy.add_student',raise_exception=True)
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


# ---------------------EDIT----------------


@login_required
@permission_required('academy.change_course',raise_exception=True)
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


@login_required
@permission_required('academy.change_trainer',raise_exception=True)
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


@login_required
@permission_required('academy.change_student',raise_exception=True)
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


# ----------------VIEW----------------------

def view_course(request,id):
    course = get_object_or_404(Course,id=id)
    print(course)
    context = {
        'course': course,
        'Title': "Course"
    }
    return render(request,'view.html',context)


@login_required
def view_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    context = {
        'trainer' : trainer,
        "Title" : 'Trainer'
    }
    return render(request,'view.html',context)


@login_required
@permission_required('academy.view_student',raise_exception=True)
def view_student(request,id):
    student = get_object_or_404(Student,id=id)
    context = {
        'student' : student,
        "Title" : 'Student'
    }    
    return render(request,'view.html',context)

# ------------------DELETE----------------------

@login_required
@permission_required('academy.delete_course',raise_exception=True)
def delete_course(request,id):
    course = get_object_or_404(Course,id=id)
    if request.method == 'POST':
        course.delete()
    return redirect('course')


@login_required
@permission_required('academy.delete_trainer',raise_exception=True)
def delete_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    if request.method == 'POST':
        trainer.delete()
    return redirect('trainer')


@login_required
@permission_required('academy.delete_student',raise_exception=True)
def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.delete()
    return redirect('student')