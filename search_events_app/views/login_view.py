from django.contrib.sessions.models import Session
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
    if request.method == 'GET':
        try:
            session = Session.objects.get(pk=request.session.session_key)
            return redirect('find_feature')
        except:
            return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            session = Session.objects.get(pk=request.session.session_key)
        except:
            if not request.session.exists(request.session.session_key):
                request.session.create()
                session = request.session
                try:
                    DBService.create_connection(username, password, session)
                    session['username'] = username
                    import ipdb; ipdb.set_trace()
                except OktaCredentialError as e:
                    return render(request, 'login.html', {'error': e.message})
                except PrestoError as e:
                    return render(request, 'login.html', {'error': e.message})
        
        return redirect('find_feature')
