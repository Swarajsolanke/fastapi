from sqlalchemy import create_engine, column , Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""SQLALCHEMY_DATABASE_URL="sqlite:///./books.db"
engine=create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(autocommit=False,autoflush=False ,bind=engine)
Base=declarative_base()
"""


URL_DATABASE="mysql+pymysql://root:veera%40123@localhost:3306/blogapplication"
engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


