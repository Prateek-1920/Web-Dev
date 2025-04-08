from django.shortcuts import render

def form(request):
    subjects = ['DS','DBS','AI','DL','ANN']
    return render(request,'student_details_app/form.html',{'sub':subjects})

def details(request):
    display_sub = request.GET.get('chosensub')
    name = request.GET.get('name')
    return render(request,'student_details_app/student_details.html',
                  {'name':name,
                   "display_sub":display_sub})
    