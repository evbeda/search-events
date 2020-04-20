release: python manage.py migrate --run-syncdb
web: gunicorn search_events.wsgi --log-file -
