from django.urls import path
from .views import home,metadata,publisher,reviews

urlpatterns = [
    path("",home,name='home'),
    path("metadata/",metadata,name='metadata'),
    path("reviews/",reviews,name='reviews'),
    path("publisher",publisher,name='publisher'),
]
