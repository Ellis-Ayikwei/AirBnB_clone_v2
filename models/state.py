#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import uuid

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
    
  
