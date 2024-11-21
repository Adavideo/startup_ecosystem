import json
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.services.linkedin_import import LinkedInImportService

def main():
    # Create database engine (using SQLite for development)
    engine = create_engine("sqlite:///linkedin_profiles.db")
    
    # Create session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    try:
        # Create import service
        import_service = LinkedInImportService(session)
        
        # Read profiles from JSON file
        with open("data/linkedin_profiles/tvss01_2024_07_16.json", "r") as f:
            profiles_data = json.load(f)
        
        # Import profiles
        imported_profiles, failed_imports = import_service.bulk_import_profiles(profiles_data)
        print(f"Successfully imported {len(imported_profiles)} profiles")
        
        # Print information about successful imports
        for profile in imported_profiles:
            print(f"\nProfile: {profile.general.get('fullName', 'Unknown')}")
            print(f"Headline: {profile.general.get('headline', 'No headline')}")
            print(f"Location: {profile.general.get('location', 'No location')}")
            print(f"Number of jobs: {len(profile.jobs)}")
            print(f"Number of skills: {len(profile.skills)}")
        
        # Print information about failed imports
        if failed_imports:
            print("\nFailed imports:")
            for failed in failed_imports:
                print(f"Profile URL: {failed['profile_url']}")
                print(f"Error: {failed['error']}\n")
            
    except Exception as e:
        print(f"Error importing profiles: {str(e)}")
        sys.exit(1)
    finally:
        session.close()

if __name__ == "__main__":
    main()
