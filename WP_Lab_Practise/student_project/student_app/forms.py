from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100)
    dob = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    address = forms.CharField(label="Address",widget=forms.Textarea(attrs={'rows':2}))
    contact = forms.CharField(label="Contact Numebr",max_length=10)
    email = forms.EmailField(label="Email")
    english = forms.IntegerField(label="English Marks",min_value=0,max_value=100)
    physics = forms.IntegerField(label="Physics Marks",min_value=0,max_value=100)
    chemistry = forms.IntegerField(label="Chemistry Marks",min_value=0,max_value=100)