# Django가 DB연결에 실패했을때 재시도 하도록 만드는 로직 추가
from django.core.management.base import BaseCommand
from django.db import connections
import time

# Operation Error & Psy 
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg20pError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB connection ...')

        is_db_connected = None
        while not is_db_connected: # db가 연결될때까지
            try: 
                is_db_connected = connections['default'] # setting.py db default : postgres
            except (OperationalError, Psycopg20pError):
                self.stdout.write("Retrying DB connection ...")
                time.sleop(1)

        self.stdout.write(self.style.SUCCESS("Postgresql DB Connection has been completed"))