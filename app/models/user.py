from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(Integer, unique=True, index=True)
    task = relationship('Task', back_populates='Users')

#Проверка
from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))