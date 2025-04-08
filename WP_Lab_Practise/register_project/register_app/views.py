from django.shortcuts import render

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        
        return render(request,'register_app/success.html',{
            'username' : username,
            'email' : email,
            'contact' : contact,
        })
        
    return render(request,'register_app/register.html')
    