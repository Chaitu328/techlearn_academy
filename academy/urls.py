from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course,name='course'),
    path('trainers/', views.trainer,name='trainer'),
    path('students/', views.student,name='student'),

    path('courses/add',views.add_course,name='add_course'),
    path('trainers/add',views.add_trainer,name='add_trainer'),
    path('students/add',views.add_student,name='add_student'),

    path('courses/edit/<int:id>/',views.edit_course,name='edit_course'),
    path('trainers/edit/<int:id>/',views.edit_trainer,name='edit_trainer'),
    path('students/edit/<int:id>/',views.edit_student,name='edit_student'),

    path('courses/view/<int:id>/',views.view_course,name='view_course'),
    path('trainers/view/<int:id>/',views.view_trainer,name='view_trainer'),
    path('students/view/<int:id>/',views.view_student,name='view_student'),
    
    path('courses/delete/<int:id>/',views.delete_course,name='delete_course'),
    path('trainers/delete/<int:id>/',views.delete_trainer,name='delete_trainer'),
    path('students/delete/<int:id>/',views.delete_student,name='delete_student'),
]