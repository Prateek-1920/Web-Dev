from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    form = StudentForm()
    student_data = ""
    percentage = None

    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            dob = form.cleaned_data["dob"]
            address = form.cleaned_data["address"]
            contact= form.cleaned_data["contact"]
            email= form.cleaned_data["email"]
            english = form.cleaned_data["english"]
            physics = form.cleaned_data["physics"]
            chemistry= form.cleaned_data["chemistry"]
           
            total = english+physics+chemistry
            percentage = (total*100)/300
            
            student_data = (
                f"Name:{name}\n"
                f"DOB:{dob}\n"
                f"Address:{address}\n"
                f"Contact:{contact}\n"
                f"Email:{email}\n"
                f"Marks: English{english}   Physics{physics}    Chemistry{chemistry}\n"
                f"Total Percentage {percentage :.2f}%\n"
            )
            
    return render(request,"student_app/student_form.html",{"form":form,"student_data":student_data,"percentage":percentage})
