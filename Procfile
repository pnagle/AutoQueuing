web: gunicorn --pythonpath="$PWD/AutoQueuing" AutoQueuing.wsgi 
worker: celery -A AutoQueuing worker -l info

