#!/usr/bin/python3
""" Define and import the State model """
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """ Defining a class State to be linked to the db table """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
