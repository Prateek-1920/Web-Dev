from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def student_input(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request,'student_data_app/student_submitted.html',{'name':student.name})
    else:
        form = StudentForm()
    return render(request,'student_data_app/student_form.html',{'form':form})

def show_students(request):
    students = Student.objects.all()
    return render(request,'student_data_app/student_list.html',{'students':students})