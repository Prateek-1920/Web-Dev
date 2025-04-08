from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.IntegerField(label="Enter first number")
    num2 = forms.IntegerField(label="Enter second number")
    op = forms.ChoiceField(
        choices=[('+','Addition'),
                 ('-','Subtraction'),
                 ('*','Multiplication'),
                 ('/','Division')],
        label="Select Operation"
    )