import logging
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_menu_app.settings')
django.setup()

from django_menu_app.models import MenuItem


def add_menu_items() -> bool:
    """
    Creates and adds menu items to the database.
    """
    try:
        main_menu = MenuItem.objects.create(name='Main Menu', url='/', parent=None)
        about_us = MenuItem.objects.create(name='About Us', url='/about/', parent=main_menu)
        services = MenuItem.objects.create(name='Services', url='/services/', parent=main_menu)
        contacts = MenuItem.objects.create(name='Contacts', url='/contacts/', parent=main_menu)

        web_dev = MenuItem.objects.create(name='Web Development', url='/services/web-dev/', parent=services)
        mobile_apps = MenuItem.objects.create(name='Mobile Applications', url='/services/mobile-apps/', parent=services)

        secondary_menu = MenuItem.objects.create(name='Secondary Menu', url='/secondary/', parent=None)
        news = MenuItem.objects.create(name='News', url='/secondary/news/', parent=secondary_menu)
        blog = MenuItem.objects.create(name='Blog', url='/secondary/blog/', parent=secondary_menu)
        portfolio = MenuItem.objects.create(name='Portfolio', url='/secondary/portfolio/', parent=secondary_menu)

        web_projects = MenuItem.objects.create(name='Web Projects', url='/secondary/portfolio/web-projects/',
                                               parent=portfolio)
        mobile_apps_portfolio = MenuItem.objects.create(name='Mobile Apps',
                                                        url='/secondary/portfolio/mobile-apps/', parent=portfolio)
        return True
    except Exception as e:
        logging.exception(e)
        return False


if __name__ == '__main__':
    if add_menu_items():
        logging.info("Menu successfully added to the database.")
    else:
        exit(1)
