from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


class Database:
    def __init__(self, db_url="sqlite:///library.db"):
        self.engine = create_engine(db_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self._initialize_db()

    def _initialize_db(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()
