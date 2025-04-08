from django.shortcuts import render
from .forms import employeeform
import datetime

def check(request):
    form = employeeform()
    promotion = None
    
    if request.method=="POST":
        form = employeeform(request.POST)
        if form.is_valid():
            doj = form.cleaned_data['date_of_join']
            today = datetime.date.today()
            
            exp = (today-doj).days/365
            if exp>=5:
                promotion="YES"
            else:
                promotion="NO"
    return render(request,"employee_app/employee_form.html",{"form":form,"promotion_status":promotion})

