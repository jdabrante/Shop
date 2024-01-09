runserver:
    python manage.py runserver

makemigrations app="": 
    python manage.py makemigrations {{ app }}

migrate: 
    python manage.py migrate

rabbitmq: 
    sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

celery:
    celery -A myshop worker -l info