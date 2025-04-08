from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_event,name='add_event'),
    path('part/',views.add_part,name='add_part'),
    path('show/',views.show_events,name='show_events')
]
