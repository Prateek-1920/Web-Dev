from django.shortcuts import render
from .forms import CaptchaForm

failed_attempts = 0

def captcha_veiw(request):
    global failed_attempts
    message = ""
    
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        
        if form.is_valid():
            message = "CAPTCHA MATCHED"
            failed_attempts = 0
        else:
            failed_attempts+=1
            message=f"CAPTCHA FAILED. ATTEMPTS LEFT = {3-failed_attempts}"
    else:
        form = CaptchaForm()
        
    return render(request,"captcha_app/captcha_form.html" ,{
        "form":form,
        "message":message,
        "disabled_input":failed_attempts>=3,
    })
