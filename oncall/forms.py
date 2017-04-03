from django.db import models
from django.forms import ModelForm, DateTimeInput, ModelChoiceField, Select
from .models import Event, EventType


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('event_name','event_type','event_start','event_end','event_notes','user')
        widgets = {
            'event_start': DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M:%S'),
            'event_end': DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M:%S')
        }


class EventTypeForm(ModelForm):
    class Meta:
        model = EventType
        fields = ('event_type_name',)