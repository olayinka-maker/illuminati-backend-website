from pydantic import BaseModel, EmailStr
from typing import Optional


class ContactBase(BaseModel):
    full_name: str
    email: EmailStr
    country: Optional[str] = None
    state_of_origin: Optional[str] = None
    date_of_birth: Optional[str] = None
    age: Optional[str] = None
    occupation: Optional[str] = None
    income: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    how_hear: Optional[str] = None
    about: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactRead(ContactBase):
    id: int

    class Config:
        orm_mode = True
