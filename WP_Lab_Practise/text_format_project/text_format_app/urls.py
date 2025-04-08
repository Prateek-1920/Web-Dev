from django.urls import path
from text_format_app.views import text_formatter

urlpatterns = [
    path('',text_formatter,name='text_formatter')
]
 