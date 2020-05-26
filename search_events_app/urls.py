from django.urls import path

from search_events_app.views import (
    EventListView,
    login,
    logout,
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
