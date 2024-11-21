from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LinkedInProfile(Base):
    __tablename__ = "linkedin_profiles"

    id = Column(Integer, primary_key=True, index=True)
    profile_url = Column(String, unique=True, index=True)  # Using profile_url as unique identifier
    query = Column(String)  # Original query URL
    
    # General Information
    general = Column(JSON)  # Stores all general profile information
    
    # Professional Information
    jobs = Column(JSON)  # List of job experiences
    schools = Column(JSON)  # List of education details
    skills = Column(JSON)  # List of skills with endorsements
    
    # Additional Information
    interests = Column(JSON)  # All interests (companies, schools, influencers, groups)
    accomplishments = Column(JSON)  # Courses, languages, and other accomplishments
    recommendations = Column(JSON)  # Given and received recommendations
    licenses = Column(JSON)  # Professional licenses and certifications
    
    # Vector search
    vector_embedding = Column(Text, nullable=True)  # For RAG functionality
    
    # Timestamps
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
