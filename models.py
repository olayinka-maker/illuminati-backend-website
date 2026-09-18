from sqlalchemy import Column, Integer, String, Text
from database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, index=True)
    country = Column(String(100), nullable=True)
    state_of_origin = Column(String(100), nullable=True)
    date_of_birth = Column(String(50), nullable=True)
    age = Column(String(10), nullable=True)
    occupation = Column(String(200), nullable=True)
    income = Column(String(100), nullable=True)
    gender = Column(String(50), nullable=True)
    phone_number = Column(String(50), nullable=True)
    address = Column(Text, nullable=True)
    how_hear = Column(Text, nullable=True)
    about = Column(Text, nullable=True)
