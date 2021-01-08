
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(String(40))
    height = Column(String(40))
    def __repr__(self):
        return "<Student(name='%s', age='%s', height='%s')>" % (
            self.name, self.age, self.height)