from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# psql engine
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(engine)

# use the session
# with Session() as session:
    # session.add(some_object)