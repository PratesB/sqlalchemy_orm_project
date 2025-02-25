import os
from dotenv import load_dotenv

from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

load_dotenv()

def session_return():
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    DB = os.getenv("DB")

    CONNECTION = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

    engine = create_engine(CONNECTION)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerRegister():
    @classmethod
    def check_data(cls, name, email, password):
        if len(name) > 50 or len(name) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(password) > 100 or len(password) < 6:
            return 4
    
        return 1
    

    @classmethod
    def register(cls, name, email, password):
        session = session_return()
        user = session.query(Register).filter(Register.email==email).all()

        if len(user) > 0:
            return 5
        
        verified_data = cls.check_data(name, email, password)

        if verified_data != 1:
            return verified_data
        
        try:
            password = hashlib.sha256(password.encode()).hexdigest()
            save_new_user = Register(name=name, email=email, password=password)
            session.add(save_new_user)
            session.commit()
            return 1
        
        except:
            return 6
        


class ControllerLogin():
    @classmethod
    def login(cls, email, password):
        session = session_return()

        password = hashlib.sha256(password.encode()).hexdigest()
        logged = session.query(Register).filter(Register.email==email).filter(Register.password == password).all()

        if len(logged) == 1:
            return {'You are logged. Your ID number is': logged[0].id}
        else:
            return False



class ControllerDelete():
    @classmethod
    def delete_user(cls, email, password):
        session = session_return()

        try:
            user = session.query(Register).filter(Register.email==email).first()
            if not user:
                return 7


            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if user.password != password_hash:
                return 8
        


            session.delete(user)
            session.commit()
            return 1
        except Exception as e:
            session.rollback()
            return 6
                