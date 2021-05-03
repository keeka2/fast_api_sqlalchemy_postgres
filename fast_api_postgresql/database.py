from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
connecting to postgresql
1. Create the SQLAlchemy engine(use this engine in other places.)
2. Create a SessionLocal class(SessionLocal class will be a database session)
"""

POSTGRES_DATABASE_URL = "postgresql://kimjunsung:1234@localhost:5432/postgres"

# 엔진은 선언만 해서 연결이 되는게 아니라 첫 실행이 될 때 연결
engine = create_engine(
    POSTGRES_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()