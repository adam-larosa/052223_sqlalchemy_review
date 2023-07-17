from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine( 'sqlite:///funstuff.db' )
Session = sessionmaker( bind = engine )

session = Session()



class Fighter( Base ):
    __tablename__ = 'fighters'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )

    age = Column( Integer() )

    
