import pytest
from datetime import datetime
from datetime import timezone as tz
from app.models.profile import LinkedInProfile

def test_create_linkedin_profile(db_session):
    # Create test profile data
    profile = LinkedInProfile(
        profile_url="https://www.linkedin.com/in/johndoe/",
        query="https://www.linkedin.com/in/johndoe/",
        general={
            "imgUrl": "https://example.com/photo.jpg",
            "firstName": "John",
            "lastName": "Doe",
            "fullName": "John Doe",
            "headline": "Software Engineer",
            "location": "San Francisco, CA"
        },
        jobs=[{
            "companyUrl": "https://www.linkedin.com/company/techcorp/",
            "companyName": "Tech Corp",
            "jobTitle": "Senior Software Engineer",
            "dateRange": "2020 - Present",
            "description": "Leading software development team"
        }],
        schools=[{
            "schoolUrl": "https://www.linkedin.com/school/university-of-tech/",
            "schoolName": "University of Tech",
            "degree": "BS Computer Science",
            "dateRange": "2012 - 2016"
        }],
        skills=[{
            "name": "Python",
            "endorsements": 50
        }],
        interests={
            "companies": [{"name": "Tech Corp", "url": "https://www.linkedin.com/company/techcorp/"}],
            "schools": [{"name": "University of Tech", "url": "https://www.linkedin.com/school/university-of-tech/"}]
        },
        accomplishments={
            "courses": ["Machine Learning", "Data Science"],
            "languages": ["English", "Spanish"]
        },
        recommendations={
            "receivedRecommendations": [],
            "givenRecommendations": []
        },
        licenses=[],
        created_at=datetime.now(tz.utc),
        updated_at=datetime.now(tz.utc)
    )
    
    # Add profile to database
    db_session.add(profile)
    db_session.commit()
    
    # Query the profile
    saved_profile = db_session.query(LinkedInProfile).filter_by(profile_url="https://www.linkedin.com/in/johndoe/").first()
    
    # Assert profile was saved correctly
    assert saved_profile is not None
    assert saved_profile.general["fullName"] == "John Doe"
    assert saved_profile.general["headline"] == "Software Engineer"
    assert len(saved_profile.jobs) == 1
    assert saved_profile.jobs[0]["companyName"] == "Tech Corp"
    assert len(saved_profile.skills) == 1
    assert saved_profile.skills[0]["name"] == "Python"

def test_unique_profile_url_constraint(db_session):
    # Create first profile
    profile1 = LinkedInProfile(
        profile_url="https://www.linkedin.com/in/johndoe/",
        query="https://www.linkedin.com/in/johndoe/",
        general={"fullName": "John Doe"},
        created_at=datetime.now(tz.utc),
        updated_at=datetime.now(tz.utc)
    )
    db_session.add(profile1)
    db_session.commit()
    
    # Try to create second profile with same profile_url
    profile2 = LinkedInProfile(
        profile_url="https://www.linkedin.com/in/johndoe/",
        query="https://www.linkedin.com/in/johndoe/",
        general={"fullName": "Jane Doe"},
        created_at=datetime.now(tz.utc),
        updated_at=datetime.now(tz.utc)
    )
    
    # Should raise an integrity error
    with pytest.raises(Exception):
        db_session.add(profile2)
        db_session.commit()

def test_update_linkedin_profile(db_session):
    # Create initial profile
    profile = LinkedInProfile(
        profile_url="https://www.linkedin.com/in/johndoe/",
        query="https://www.linkedin.com/in/johndoe/",
        general={"fullName": "John Doe", "headline": "Software Engineer"},
        created_at=datetime.now(tz.utc),
        updated_at=datetime.now(tz.utc)
    )
    db_session.add(profile)
    db_session.commit()
    
    # Update profile
    saved_profile = db_session.query(LinkedInProfile).filter_by(profile_url="https://www.linkedin.com/in/johndoe/").first()
    general = dict(saved_profile.general)  # Create a new dict
    general["headline"] = "Senior Software Engineer"
    saved_profile.general = general  # Assign the new dict to trigger SQLAlchemy change detection
    saved_profile.updated_at = datetime.now(tz.utc)
    db_session.commit()
    
    # Verify update
    updated_profile = db_session.query(LinkedInProfile).filter_by(profile_url="https://www.linkedin.com/in/johndoe/").first()
    assert updated_profile.general["headline"] == "Senior Software Engineer"
