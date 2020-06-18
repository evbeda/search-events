from django.shortcuts import (
    redirect,
)
from django.core.exceptions import SuspiciousOperation

from search_events_app.services.db.db_service import DBService


def logout(request):
    if request.method == 'POST':
        DBService.disconnect(request.session)
        return redirect('login')
    else:
        raise SuspiciousOperation()
