from sqlalchemy import String, DateTime, Integer, NUMERIC
from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

class Payments(Base):
    __tablename__ = "payments"
    id = mapped_column(Integer, primary_key=True, unique=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    amount = mapped_column(NUMERIC(10,2), nullable=False)
    stripe_payment_id = mapped_column(String(100), nullable=False)
    status = mapped_column(String(20), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)
