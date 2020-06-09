from django.urls import path
from django.views.generic import RedirectView

from search_events_app.views import (
    EventListView,
    login,
    logout,
)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='find_feature', permanent=False)),
    path('FindFeature/', EventListView.as_view(), name='find_feature'),
    path('SpecificEvent/', EventListView.as_view(), name='specific_event'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
