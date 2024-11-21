import pytest
from datetime import datetime
from datetime import timezone as tz
from app.models.profile import LinkedInProfile
from app.services.linkedin_import import LinkedInImportService

@pytest.fixture
def import_service(db_session):
    return LinkedInImportService(db_session)

def test_import_single_profile(import_service, db_session):
    # Test data
    profile_data = {
        "general": {
            "profileUrl": "https://www.linkedin.com/in/johndoe/",
            "fullName": "John Doe",
            "headline": "Software Engineer",
            "location": "San Francisco, CA"
        },
        "jobs": [{
            "companyUrl": "https://www.linkedin.com/company/techcorp/",
            "companyName": "Tech Corp",
            "jobTitle": "Software Engineer"
        }],
        "skills": [{
            "name": "Python",
            "endorsements": 50
        }],
        "query": "https://www.linkedin.com/in/johndoe/",
        "timestamp": "2024-07-16T04:03:52.107Z"
    }

    # Import profile
    profile = import_service.import_profile(profile_data)

    # Verify profile was imported correctly
    assert profile.profile_url == "https://www.linkedin.com/in/johndoe/"
    assert profile.general["fullName"] == "John Doe"
    assert profile.general["headline"] == "Software Engineer"
    assert profile.jobs[0]["companyName"] == "Tech Corp"

def test_bulk_import_profiles(import_service, db_session):
    # Test data
    profiles_data = [
        {
            "general": {
                "profileUrl": "https://www.linkedin.com/in/johndoe/",
                "fullName": "John Doe",
                "headline": "Software Engineer"
            },
            "query": "https://www.linkedin.com/in/johndoe/"
        },
        {
            "general": {
                "profileUrl": "https://www.linkedin.com/in/janesmith/",
                "fullName": "Jane Smith",
                "headline": "Product Manager"
            },
            "query": "https://www.linkedin.com/in/janesmith/"
        }
    ]

    # Import profiles
    imported_profiles = import_service.bulk_import_profiles(profiles_data)

    # Verify correct number of profiles were imported
    assert len(imported_profiles) == 2

    # Verify profiles were saved in database
    profiles = db_session.query(LinkedInProfile).all()
    assert len(profiles) == 2
    assert {p.general["fullName"] for p in profiles} == {"John Doe", "Jane Smith"}

def test_update_existing_profile(import_service, db_session):
    # Create initial profile
    profile_data = {
        "general": {
            "profileUrl": "https://www.linkedin.com/in/johndoe/",
            "fullName": "John Doe",
            "headline": "Software Engineer"
        },
        "query": "https://www.linkedin.com/in/johndoe/"
    }
    profile = import_service.import_profile(profile_data)

    # Update profile data
    updated_data = {
        "general": {
            "profileUrl": "https://www.linkedin.com/in/johndoe/",
            "fullName": "John Doe",
            "headline": "Senior Software Engineer"
        },
        "query": "https://www.linkedin.com/in/johndoe/"
    }

    # Update profile
    updated_profile = import_service.import_profile(updated_data)

    # Verify update
    assert updated_profile.general["headline"] == "Senior Software Engineer"
    assert updated_profile.general["fullName"] == "John Doe"  # Original data should remain unchanged

def test_get_profile_by_url(import_service, db_session):
    # Create test profile
    profile_data = {
        "general": {
            "profileUrl": "https://www.linkedin.com/in/johndoe/",
            "fullName": "John Doe",
            "headline": "Software Engineer"
        },
        "query": "https://www.linkedin.com/in/johndoe/"
    }
    import_service.import_profile(profile_data)

    # Get profile by URL
    profile = import_service.get_profile_by_url("https://www.linkedin.com/in/johndoe/")

    # Verify profile was retrieved correctly
    assert profile is not None
    assert profile.general["fullName"] == "John Doe"
    assert profile.general["headline"] == "Software Engineer"

    # Test nonexistent profile
    nonexistent = import_service.get_profile_by_url("https://www.linkedin.com/in/nonexistent/")
    assert nonexistent is None
