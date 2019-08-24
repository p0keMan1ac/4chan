import logging
from Database.base_database_wrapper import BaseDatabaseWrapper
from sqlalchemy import create_engine


class DatabaseEngine(BaseDatabaseWrapper):

    DATABASE_ENGINE = {
        'sqlite': {
            'connection_string': 'sqlite:////{DB}',
        },
        'postgres': {
            'connection_string': 'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
        }
    }

    database_engine = None

    def __init__(self, database_type='sqlite', path_to_database_file='', database_user='', database_password='',
                 database_port='',
                 database_host='', database_name='', autocommit=True):
        super().__init__()
        self.database_type = database_type.lower()
        self.path_to_database_file = path_to_database_file
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_port = database_port
        self.database_name = database_name
        self.autocommit = autocommit
        self.database_connection_string = None

    def set_engine(self):
        self.check_engine()
        if self.database_type == 'sqlite':
            self.database_connection_string = self.DATABASE_ENGINE[self.database_type]['connection_string'].format(
                DB=self.path_to_database_file)
        else:
            self.database_connection_string = self.DATABASE_ENGINE[self.database_type]['connection_string'].format(
                DB_USER=self.database_user, DB_PASSWORD=self.database_password, DB_HOST=self.database_host,
                DB_PORT=self.database_port, DB_NAME=self.database_name)
        try:
            self.database_engine = create_engine(self.database_connection_string)
        except Exception as error:
            error_msg = repr(error)
            logging.error(f"Could not create engine.ERROR=[{error_msg}].")
            exit(code=1)

    def get_engine(self):
        return self.database_engine

    def get_all_tables(self):
        return self.database_engine.table_names()

    def check_engine(self):
        if self.database_type in self.DATABASE_ENGINE.keys():
            logging.info(f'Engine of database is available for: {self.database_type}')
        else:
            logging.error(f"Called engine: {self.database_type} not available for DatabaseWrapper.")
            raise Exception(f'Called engine {self.database_type} is not available.')

    def __enter__(self):
        self.set_engine()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.database_engine.dispose()
            logging.error(f'There was error during connection to database Exception[{exc_val}].')
            raise Exception('There was error during connection to database')
        else:
            self.database_engine.dispose()
