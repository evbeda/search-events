from django.shortcuts import (
    render,
    redirect
)

from search_events_app.services.db.db_service import DBService
from search_events_app.exceptions import (
    PrestoError,
    OktaCredentialError,
)


def login(request):
    session = request.session

    if request.method == 'GET':
        if DBService.is_connected(session):
            return redirect('find_feature')
        else:
            return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        session.create()
        try:
            DBService.create_connection(username, password, session)
            session['username'] = username
        except (OktaCredentialError, PrestoError) as e:
            DBService.disconnect(session)
            return render(request, 'login.html', {'error': e.message})
        return redirect('find_feature')
