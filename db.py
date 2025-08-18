from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembicstuff.models_old import Base

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/bank1"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# TODO: Run pytest to make sure it is working
# https://docs.pytest.org/en/7.1.x/getting-started.html
# https://chat.mistral.ai/chat/bc47ef88-cd09-433b-8d4f-8528dff2acc5