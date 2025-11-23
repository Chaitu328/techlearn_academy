from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course,name='course'),
    path('trainers/', views.trainer,name='trainer'),
    path('students/', views.student,name='student')
]