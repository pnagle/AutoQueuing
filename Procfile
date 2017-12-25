web: gunicorn --pythonpath="$PWD/AutoQueuing" AutoQueuing.wsgi 
worker: celery worker --app=tasks.app

