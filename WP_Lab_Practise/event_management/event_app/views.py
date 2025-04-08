from django.shortcuts import render,redirect
from .models import Event, Participant
from .forms import EventForm, PartForm


def add_event(request):
    if request.method=='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_event')
    else:
        form = EventForm()
    
    return render(request,'event_app/add_event.html',{'form':form})


def add_part(request):
    if request.method=='POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_part')
    else:
        form = PartForm()
    
    return render(request,'event_app/add_part.html',{'form':form})

def show_events(request):
    events = Event.objects.all()
    parts = Participant.objects.all()
    return render(request,'event_app/show_events.html',{'events':events, 'parts':parts})