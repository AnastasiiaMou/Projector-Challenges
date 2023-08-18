from requests import session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(
    DATABASE_URI.format(
        host="localhost",
        database="projector",
        user="ananasia",
        password="password",
        port=5432,
    )
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Users(Base):
    __tablename__ = "student"

    usersid = Column(Integer, primary_key=True)
    name = Column(String)
    user_type = Column(String)
    email = Column(String)
    password = Column(String)


class Guest(Base):
    __tablename__ = "guest"

    guestid = Column(Integer, primary_key=True)
    usersid = Column(Integer, ForeignKey("Users.usersid"))


class Host(Base):
    __tablename__ = "host"

    hostid = Column(Integer, primary_key=True)
    usersid = Column(Integer, ForeignKey("Users.usersid"))
    host_rate = Column(Integer)
    host_description = Column(String)


class Reservations(Base):
    __tablename__ = "reservations"

    reservationsid = Column(Integer, primary_key=True)
    guestid = Column(Integer, ForeignKey("Guests.guestid"))
    roomid = Column(Integer, ForeignKey("Room.roomid"))
    check_in = Column()
    check_out = Column()
    total_price = Column(float)


class Review(Base):
    __tablename__ = "review"

    reviewid = Column(Integer, primary_key=True)
    guestid = Column(Integer, ForeignKey("Guests.guestid"))
    hostid = Column(Integer, ForeignKey("Host.hostid"))
    reservationsid = Column(Integer, ForeignKey("Reservations.reservationsid"))
    rating = Column(float)
    review_text = Column(String)
    review_date = Column()


class Room(Base):
    __tablename__ = "room"

    roomid = Column(Integer, primary_key=True)
    hostid = Column(Integer, ForeignKey("Host.hostid"))
    price = Column(float)
    AC = Column()
    refrigerator = Column()


