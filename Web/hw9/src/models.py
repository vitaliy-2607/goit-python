from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    phones = relationship('Phone', back_populates='contact')
    emails = relationship('Email', back_populates='contact')




class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(15), unique=True, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='phones')


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    mail = Column(String(254), unique=True, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='emails')


