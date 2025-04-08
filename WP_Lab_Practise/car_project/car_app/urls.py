from django.urls import path
from . import views

urlpatterns = [
    path('',views.car_form,name="car_form"),
    path('car_details/',views.car_details,name="car_details"),
]
