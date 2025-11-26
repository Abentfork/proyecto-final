from models.user import Users
from models.bet import Bets
from models.game import Games
from models.payment import Payments
from database import Base, engine


if __name__ == "__main__" :
    Base.metadata.create_all(bind=engine)
    
