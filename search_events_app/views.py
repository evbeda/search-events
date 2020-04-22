from django.shortcuts import render
from django.views.generic.list import ListView

from .services.dummy_api import DummyApi


# Create your views here.
class EventListView(ListView):
    template_name = 'event_list.html'

    def get_queryset(self):
        return DummyApi().get()
