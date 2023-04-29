from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from app.database.database import DataBase


class Users(DataBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(300), unique=True)
    password = Column(String(300))
    fio = Column(String(300))
    code = Column(String(300))
    flat = Column(String(300))
    house = Column(String(300))


class Documents(DataBase):
    __tablename__ = "docs"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    user_id = Column(Integer, ForeignKey("users.id"))


class Counters(DataBase):
    __tablename__ = "counters"
    id = Column(Integer, primary_key=True)
    number = Column(String(300))
    user_id = Column(Integer, ForeignKey("users.id"))
    add_time = Column(DateTime, server_default=func.now())


class CounterValues(DataBase):
    __tablename__ = "counter_values"
    id = Column(Integer, primary_key=True)
    value = Column(String(300))
    user_id = Column(Integer, ForeignKey("users.id"))
    counter_id = Column(Integer, ForeignKey("counters.id"))
    add_time = Column(DateTime, server_default=func.now())
