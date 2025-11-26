from sqlalchemy import String, DateTime, Integer, Numeric
from datetime import datetime
from database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Bets database model
class Bets(Base):
    __tablename__ = "bets"
    id = mapped_column(Integer, primary_key=True, unique=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    game_id = mapped_column(Integer, ForeignKey("games.id"), nullable=False)
    bet_amount = mapped_column(Numeric(10,2), nullable=False)
    win_amount = mapped_column(Numeric(10,2), nullable=False)
    outcome = mapped_column(String(20), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)

    # Relations for easy consults
    user = relationship("Users", back_populates="bets")
    game = relationship("Games", back_populates="bets")
