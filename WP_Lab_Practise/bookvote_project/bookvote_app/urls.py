from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.vote_view,name='vote_view')
]
