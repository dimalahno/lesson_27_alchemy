from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # price = Column(Float, nullable=True)
