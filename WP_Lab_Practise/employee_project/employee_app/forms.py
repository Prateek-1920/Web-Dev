from django import forms
import datetime

class employeeform(forms.Form):
    employees = [
        ('E101','John Doe'),
        ('E102','Alice Smith'),
        ('E103','Bob John'),
    ]
    
    employee_id = forms.ChoiceField(choices=employees,label="Employee ID")
    date_of_join = forms.DateField(
        label="Date of joining",
        widget=forms.DateInput(attrs={'type':'date'})
    )