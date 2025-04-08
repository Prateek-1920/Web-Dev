from django import forms
from .models import Event, Participant

class EventForm(forms.ModelForm):    
    class Meta:
        model = Event
        fields = '__all__'
        
class PartForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
