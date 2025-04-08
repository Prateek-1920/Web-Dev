from django.urls import path
from .views import captcha_veiw

urlpatterns = [
    path("",captcha_veiw,name="captcha")
]
