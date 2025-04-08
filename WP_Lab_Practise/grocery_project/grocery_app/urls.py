from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.grocery_form,name='grocery_form'),
]
