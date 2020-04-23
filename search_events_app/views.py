from django.shortcuts import render
from django.views.generic.list import ListView

from .services.api_service import get_events


# Create your views here.
class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        return get_events
