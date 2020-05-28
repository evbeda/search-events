from django.shortcuts import (
    redirect,
)
from django.core.exceptions import SuspiciousOperation

from search_events_app.services.db.db_connection_manager import ConnectionManager


def logout(request):
    if request.method == 'POST':
        ConnectionManager.disconnect()
        return redirect('login')
    else:
        raise SuspiciousOperation()
