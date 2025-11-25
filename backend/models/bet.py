from sqlalchemy import String, DateTime, Integer, NUMERIC
from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey

class Bets(Base):
    __tablename__ = "bets"
    id = mapped_column(Integer, primary_key=True, unique=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    game_id = mapped_column(Integer, ForeignKey("games.id"), nullable=False)
    bet_amount = mapped_column(NUMERIC(10,2), nullable=False)
    win_amount = mapped_column(NUMERIC(10,2), nullable=False)
    outcome = mapped_column(String(20), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)
    