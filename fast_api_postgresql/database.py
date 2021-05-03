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
    POSTGRES_DATABASE_URL, pool_size=20,pool_recycle=500, max_overflow=20, echo=True
)

"""
Session 클래스를 factory 패턴으로 생성
Session 클래스는 새 객체를 만들어서 데이터베이스와 연결이 됨
데이터베이스와의 대화가 필요할 때 Session을 불러서 쓰면 된다
처음으로 사용될 때 Engine과 연결되고 모든 변경을 커밋하고 세션을 종료할 때까지 열려
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
ORM은 처음 데이터베이스 테이블을 쓸 수 있게 설정한 다음 직접 정의한 클래스와 매핑을 하게 됨
Declarative를 통해 클래스를 생성하고 실제 데이터베이스 데이블에 연결을 함
models.py에서 Base를 상속받은 클래스와 실제 데이터베이스 테이블과 연결 됨
"""
Base = declarative_base()

if __name__=="__main__":
    result_list = engine.execute("SELECT * FROM users;")
    for result in result_list:
        print(result)

    from fast_api_postgresql import models
    db = SessionLocal()
    print(db)
    print(db.query(models.User).filter(models.User.email == "nikolai@gmail.com").first())