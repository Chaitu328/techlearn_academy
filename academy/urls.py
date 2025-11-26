from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course,name='course'),
    path('trainers/', views.trainer,name='trainer'),
    path('students/', views.student,name='student'),
    path('courses/add',views.add_course,name='add_course'),
    path('trainers/add',views.add_trainer,name='add_trainer'),
    path('students/add',views.add_student,name='add_student')   
]