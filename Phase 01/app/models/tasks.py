from sqlalchemy import Boolean, Integer, String, Text, ForeignKey, Column
from ..database.db import Base

"""
SQLAlchemy models are Python classes that represent database tables in a relational database like PostgreSQL. 
Each model class corresponds to a single table, and its attributes define the table’s columns (e.g., id, name, email).

Key Concept: Models map Python classes to database tables, enabling you to work with data as objects. 
For example, a User model represents the "users" table, and creating a 
User object in Python translates to inserting a row in that table.

"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_done = Column(Boolean)