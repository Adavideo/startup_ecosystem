from sqlalchemy import create_engine
from app.models.profile import Base

def main():
    # Create database engine (using SQLite for development)
    engine = create_engine("sqlite:///linkedin_profiles.db")
    
    # Create all tables
    Base.metadata.create_all(engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    main()
