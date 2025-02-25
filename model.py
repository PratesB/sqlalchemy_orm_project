import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB = os.getenv("DB")

CONNECTION = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONNECTION)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()



class Register(Base):
    __tablename__ = 'Register'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(200))
    password = Column(String(100))


Base.metadata.create_all(engine)