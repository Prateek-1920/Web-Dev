from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.product_form,name="product_form"),
    path('',views.show_bill,name="show_bill"),
]
