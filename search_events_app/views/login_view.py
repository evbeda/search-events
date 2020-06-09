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
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            DBService.create_connection(username, password)
            return redirect('find_feature')
        except OktaCredentialError as e:
            return render(request, 'login.html', {'error': e.message})
        except PrestoError as e:
            return render(request, 'login.html', {'error': e.message})
