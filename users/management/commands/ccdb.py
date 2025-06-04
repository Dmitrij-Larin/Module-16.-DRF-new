import pyodbc
from django.core.management import BaseCommand

from config.settings import DATABASE, USER, PASSWORD, HOST, DRIVER, PAD_DATABASE


class Command(BaseCommand):
    """
    Создание БД
    """

    def handle(self, *args, **options):
        """
        Параметры для создания БД
        """
        ConnectionString = f"""
                            DRIVER={DRIVER};
                            SERVER={HOST};
                            DATABASE={PAD_DATABASE};
                            UID={USER};
                            PWD={PASSWORD};
                            """

        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.Error as e:
            print(e)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr"CREATE DATABASE {DATABASE};")
            except pyodbc.Error as e:
                print(e)
            else:
                print(f"База данных {DATABASE} успешно создана")
