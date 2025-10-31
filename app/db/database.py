from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Temporary fake database for testing
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@company.com",
        "role": "ADMIN",
        "hashed_password": "$2b$12$hashed_password_here",
        "is_disabled": False,
        "id": 1
    },
    "hr_manager": {
        "username": "hr_manager",
        "email": "hr@company.com",
        "role": "HR",
        "hashed_password": "$2b$12$hashed_password_here",
        "is_disabled": False,
        "id": 2
    },
    "john_doe": {
        "username": "john_doe",
        "email": "john@example.com",
        "role": "USER",
        "hashed_password": "$2b$12$hashed_password_here",
        "is_disabled": False,
        "id": 3
    }
}
