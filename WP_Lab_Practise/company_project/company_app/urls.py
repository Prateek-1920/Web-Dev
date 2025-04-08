from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_works, name='insert_works'),
    path('search/', views.search_company, name='search_company'),
]
