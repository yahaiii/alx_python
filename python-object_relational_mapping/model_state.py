from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#create class State
class State(Base):
    """
     This class inherits from SQLAlchemy's declarative base class and maps to the 'states' table.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.

    Args:
        Base (DeclarativeMeta): The base class for declarative models from SQLAlchemy.
        """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
