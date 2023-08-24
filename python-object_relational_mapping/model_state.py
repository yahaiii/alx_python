"""
Represents a State table in the database.
"""


import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a database engine using SQLAlchemy's create_engine function
# It connects to a MySQL database using the provided username, password, and database name
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

# Create a base class for declarative models
Base = declarative_base()

class State(Base):
    """
    Represents a State table in the database.
    
    It defines columns for 'id' and 'name'.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    """
    This block creates the database tables when the script is run directly.
    """
    Base.metadata.create_all(engine)
