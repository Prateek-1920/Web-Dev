from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('add_book',views.add_book,name='add_book'),
    path('add_borrower/',views.add_borrower,name='add_borrower'),
    path('issue_book/',views.issue_book,name='issue_book'),
]