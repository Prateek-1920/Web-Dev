from django.urls import include, path
from . import views

urlpatterns = [
    path('add_author/',views.add_author,name='add_author'),
    path('add_book/',views.add_book,name='add_book'),
    path('view_books/',views.view_books,name='view_books'),
]
