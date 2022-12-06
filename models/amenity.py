#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
        Anemity class
    """
    __tablename__ = 'anemities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
