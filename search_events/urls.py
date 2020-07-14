"""search_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sessions.models import Session
from django.db import OperationalError
from django.urls import (
    path,
    include
)

from search_events_app import urls as search_events_app_urls


def clear_all_sessions():
    try:
        Session.objects.all().delete()
    except OperationalError:
        pass


clear_all_sessions()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(search_events_app_urls)),
]
