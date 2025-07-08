web: bash -c "python manage.py migrate --noinput && gunicorn crud_project.wsgi:application --bind 0.0.0.0:8000 --pid /var/pids/web.pid"
