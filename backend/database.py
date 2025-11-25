from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ.get("DATABASE_URL")
engine = create_engine(database_url)



SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()