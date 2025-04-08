from django.shortcuts import render
from .forms import CalculatorForm

def calculate(request):
    result = None
    if request.method=="POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            op = form.cleaned_data['op']
            
            if op=='+':
                result = num1+num2
            elif op=='-':
                result = num1-num2
            elif op=='*':
                result = num1*num2
            elif op=='/' and num2!=0:
                result = num1/num2
            else:
                result="Invalid Input"
    else:
        form=CalculatorForm()
        
    return render(request,"calculator_app/calculator.html",
                  {"form":form,
                   "result" : result})
            

