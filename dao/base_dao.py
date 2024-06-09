import psycopg2

class BaseDAO:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return psycopg2.connect(**self.db_config)