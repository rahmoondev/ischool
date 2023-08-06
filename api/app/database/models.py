from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/ischool')
SessionCreator = sessionmaker(bind=engine)
session: Session = SessionCreator()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    gender = Column(String(10))
    name = Column(String(30))
    photo = Column(String(100))
    email = Column(String(100))
    pwd = Column(String(20))
    usertype = Column(String(1))


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    usersid = Column(Integer)
    grade = Column(Integer)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    usersid = Column(Integer)
    grade = Column(Integer)


users: list[Student] = session.query(Student).all()
for u in users:
    print(u.grade)
