#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base

from models.engine.db_storage import DBStorage

# Replace with your actual database connection string
DATABASE_URL = "mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBStorage.reload

print("Tables created successfully!")
