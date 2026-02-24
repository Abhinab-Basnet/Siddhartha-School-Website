from django.shortcuts import render
from .models import Event
from datetime import date

def event_list(request):
    
    upcoming_events = Event.objects.filter(event_date__gte=date.today()).order_by('event_date')
    return render(request, 'events/event_list.html', {'events': upcoming_events})