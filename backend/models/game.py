from sqlalchemy import String, DateTime, Integer
from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column

class Games(Base):
    __tablename__ = "games"
    id = mapped_column(Integer, unique= True, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    type = mapped_column(String(20), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)