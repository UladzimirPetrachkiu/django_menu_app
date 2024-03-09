#!/bin/sh

# Run migrations
python manage.py flush --no-input
python manage.py makemigrations
python manage.py makemigrations django_menu_app
python manage.py migrate

# Create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('test', 'test@gmail.com', 'test')" | python manage.py shell
# Add menu items
python django_menu_app/scripts/add_menu_items.py

# Run server
python manage.py runserver 0.0.0.0:8000

exec "$@"
