from contextlib import contextmanager
from sqlalchemy import create_engine
from typing import Generator, Any
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.session import Session
from pathlib import Path
import os
from dotenv import load_dotenv

project_dir = Path(__file__).resolve().parent.parent
env_path = project_dir / ".env"

print("Project dir:", project_dir)

load_dotenv(env_path)

DB_URL = os.getenv("DB_URL")
SCHEMA = os.getenv("SCHEMA", "public")


engine = create_engine(
    DB_URL,
    connect_args={"options": f"-csearch_path={SCHEMA}"},
    pool_size=200,
    max_overflow=10,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

@contextmanager
def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    with get_db() as db:
        print(db)