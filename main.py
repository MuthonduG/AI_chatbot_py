from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL 
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config

url = URL.create(
    drivername="postgresql",
    username=config("essy"),
    password=config(""),
    host="localhost",
    database="mydb"
    port=5432
)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Conversation(Base):
    pass
