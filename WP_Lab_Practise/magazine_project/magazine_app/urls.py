from django.urls import path
from . import views
from .views import generate_cover

urlpatterns = [
    path('',generate_cover,name="gen"),
    path("generate/", views.generate_cover, name="cover")
]
