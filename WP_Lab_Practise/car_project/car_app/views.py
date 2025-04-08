from django.shortcuts import render

def car_form(request):
    manufacturers = ['Toyota','Lexus','BMW','Aston Martin']
    return render(request,'car_app/form.html',{'manufacturers':manufacturers})

def car_details(request):
    manufacturer = request.GET.get('id')
    model = request.GET.get('model')
    return render(request,'car_app/car_details.html',{'manufacturer':manufacturer,'model':model})
 
