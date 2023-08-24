import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a database engine using SQLAlchemy's create_engine function
# It connects to a MySQL database using the provided username, password, and database name
if __name__ == "__main__":
    # Create a base class for declarative models
    Base = declarative_base()

    class State(Base):
        """
        Represents a state entity in the database.

        This class inherits from SQLAlchemy's declarative base class and maps to the 'states' table.
        It defines the structure of the 'states' table with columns for 'id' and 'name'.

        Attributes:
            id (int): The unique identifier for the state (auto-incremented primary key).
            name (str): The name of the state, limited to 128 characters, and cannot be null.

        Args:
            Base (DeclarativeMeta): The base class for declarative models from SQLAlchemy.
        """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(128), nullable=False)
