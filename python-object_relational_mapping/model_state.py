#!/usr/bin/python3
"""Définition de la classe State liée à la table 'states' dans la base MySQL."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base est le constructeur de classe-mère pour tous les modèles
Base = declarative_base()

class State(Base):
    """Classe qui mappe la table 'states' dans la base MySQL"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
