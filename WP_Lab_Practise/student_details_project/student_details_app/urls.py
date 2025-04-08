from django.urls import path,include
from student_details_app import views

urlpatterns = [
    path('',views.form, name="form"),
    path('student_details/',views.details,name="student_details"),
]

