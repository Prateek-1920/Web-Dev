from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_input,name='student_form'),
    path('students/',views.show_students,name='show_students')
]
