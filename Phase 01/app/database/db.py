import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

Database_URL = os.getenv('DATABASE_URL')

engine = create_engine(Database_URL)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
