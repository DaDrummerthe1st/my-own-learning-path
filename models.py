from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String

Base = DeclarativeBase()

class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    customer = Column(String, nullable=False)

class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customers", back_populates="transactions")

Customers.transactions = relationship("Transactions", order_by=Transactions.id, back_populates="customer")
