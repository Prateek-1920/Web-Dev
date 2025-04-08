from django.urls import path
from . import views

urlpatterns = [
    path('',views.input_bill,name='bill'),
    path('all_bills/',views.all_bills,name='all_bills'),
]
