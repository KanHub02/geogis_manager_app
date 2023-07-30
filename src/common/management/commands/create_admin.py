from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import logging

class Command(BaseCommand):
    help = 'Create admin phone_number=+996000000000 password="adminadmin"'
    def handle(self, *args, **options):
        try:
            admin = User.objects.filter(username="admin").first()
            if admin:
                logging.info("Admin user is created")
            User.objects.create_superuser(username="admin", password="adminadmin")
            logging.info("Admin user created successfully")
        except Exception as e:
            logging.error(e)