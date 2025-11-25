from database import Base
from datetime import datetime
from sqlalchemy import Integer, String, Numeric, DateTime
from sqlalchemy.orm import mapped_column

class Users(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, unique=True)
    username = mapped_column(String(50), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False, unique=True)
    password_hash = mapped_column(String(255), nullable=False)
    credits = mapped_column(Numeric(10,2), default=0)
    created_at = mapped_column(DateTime, default=datetime.now)
    last_login = mapped_column(DateTime, nullable=False)



