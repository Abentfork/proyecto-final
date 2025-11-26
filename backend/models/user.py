from database import Base
from datetime import datetime
from sqlalchemy import Integer, String, Numeric, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# Users database model
class Users(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, unique=True)
    username = mapped_column(String(50), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False, unique=True)
    password_hash = mapped_column(String(255), nullable=False)
    credits = mapped_column(Numeric(10,2), default=0)
    created_at = mapped_column(DateTime, default=datetime.now)
    last_login = mapped_column(DateTime, nullable=True)
    
    # Relations for easy consults
    bets = relationship("Bets", back_populates="user", cascade="all, delete")
    payments = relationship("Payments", back_populates="user", cascade="all, delete")

