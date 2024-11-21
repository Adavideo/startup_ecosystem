import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.profile import Base

@pytest.fixture(scope="function")
def db_session():
    # Create an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create a new session factory
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create a new session for the test
    session = TestingSessionLocal()
    
    try:
        yield session
    finally:
        session.close()
        # Drop all tables after the test
        Base.metadata.drop_all(engine)
