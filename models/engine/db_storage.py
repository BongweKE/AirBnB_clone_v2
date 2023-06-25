#!/usr/bin/python3
""" creating a database engine"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

class DBStorage:
    '''instanciating class DBStorage.
       Attributes:
           engine(class attribute)
           session(class attribute)
    '''
    __engine = None
    __session = None
    def __init__(self):
        '''initializing class DBStorage constructor.'''
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") = test:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query all objects in our database according to cls, if none returns
           all databases objects.'''
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session).query(Amenity).all())
            objs.extend(self.__session).query(Place).all())
            objs.extend(self.__session).query(Review).all())
            objs.extend(self.__session).query(User).all())
        else:
            if type(cls) = str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        '''creates a new object in the current session.'''
        self.__session.add(obj)

    def save(self):
        '''commits all changes in the current session.'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes obj from the current database session.'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''creates all tables in the current database and initializes a new
           session.'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
