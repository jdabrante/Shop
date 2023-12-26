runserver:
    python manage.py runserver

makemigrations app="": 
    python manage.py makemigrations {{ app }}

migrate: 
    python manage.py migrate
