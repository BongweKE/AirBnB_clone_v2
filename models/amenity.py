#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    __tablename__ = "Amenity"
   name = Column(String(128), nullable=False)
