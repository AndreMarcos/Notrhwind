import psycopg2

class BaseDAO:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return psycopg2.connect(**self.db_config)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class BaseDAOSQLAlchemy:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()