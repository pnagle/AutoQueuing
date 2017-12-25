web: gunicorn --pythonpath="$PWD/AutoQueuing" AutoQueuing.wsgi 
worker: python manage.py celery worker -B -l info

