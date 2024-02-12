from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, DateTime, String, Integer, func

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    age = Column(Integer)
    note = Column(String(200))
    create_at = Column(DateTime, default=func.now())

    def __init__(name, age, note):
        self.name=name
        self.age=age
        self.note=note


metadata = Base.metadata