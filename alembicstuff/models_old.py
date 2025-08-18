import enum
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase, relationship

Base = DeclarativeBase()

class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    customer = Column(String, nullable=False)
    address = Column(String, nullable=False)
    ssn = Column(String, unique=True, nullable=False)
    account = Column(String, unique=True, nullable=False)
    #email = Column(String)
    transactions = relationship("Transactions", back_populates="customers")

class TransTypeEnum(enum.Enum):
    outgoing = "outgoing"
    incoming = "incoming"
    
class Transactions(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    amount = Column(Numeric, nullable=False)
    currency = Column(String, nullable=False)
    sender_account = Column(String, nullable=False)
    receiver_account = Column(String, nullable=False)
    sender_country = Column(String, nullable=False)
    sender_municipality = Column(String, nullable=False)
    receiver_country = Column(String, nullable=False)
    receiver_municipality = Column(String, nullable=False)
#    transaction_type = Column(Enum(TransTypeEnum), nullable=False)
    transaction_type = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    customers = relationship("Customers", back_populates="transactions")

# belongs to db.py:
# from models import Base

# DATABASE_URL = ""