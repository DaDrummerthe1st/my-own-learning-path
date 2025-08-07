from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


# belongs to db.py:
# from models import Base

# DATABASE_URL = ""