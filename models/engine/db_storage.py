#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBStorage:
    """Create tables in environment"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
        returns a dictionary of __object
        """
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elm in query:
                key = "{}.{}".format(type(elm).__name__, elm.id)
                dic[key] = elm
        else:
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User
            list_a = [State, City, User, Place, Review, Amenity]
            for a_class in list_a:
                query = self.__session.query(a_class)
                for elm in query:
                    key = "{}.{}".format(type(elm).__name__, elm.id)
                    dic[key] = elm
        return (dic)

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
