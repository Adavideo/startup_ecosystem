import json
from datetime import datetime
from datetime import timezone as tz
from typing import Dict, Any, List, Tuple
from sqlalchemy.orm import Session
from ..models.profile import LinkedInProfile

class LinkedInImportService:
    def __init__(self, db: Session):
        self.db = db

    def import_profile(self, profile_data: Dict[str, Any]) -> LinkedInProfile:
        """
        Import a LinkedIn profile from the provided data.
        
        Args:
            profile_data: Dictionary containing LinkedIn profile data
        
        Returns:
            LinkedInProfile: The imported profile object
        """
        # Check if profile already exists
        existing_profile = self.db.query(LinkedInProfile).filter_by(
            profile_url=profile_data.get('general', {}).get('profileUrl')
        ).first()
        
        if existing_profile:
            # Update existing profile
            existing_profile.general = profile_data.get('general', {})
            existing_profile.jobs = profile_data.get('jobs', [])
            existing_profile.schools = profile_data.get('schools', [])
            existing_profile.skills = profile_data.get('skills', [])
            existing_profile.interests = profile_data.get('interests', {})
            existing_profile.accomplishments = profile_data.get('accomplishments', {})
            existing_profile.recommendations = profile_data.get('recommendations', {})
            existing_profile.licenses = profile_data.get('licenses', [])
            existing_profile.query = profile_data.get('query', '')
            existing_profile.updated_at = datetime.now(tz.utc)
            
            self.db.commit()
            self.db.refresh(existing_profile)
            return existing_profile
        
        # Create new profile
        profile = LinkedInProfile(
            profile_url=profile_data.get('general', {}).get('profileUrl'),
            general=profile_data.get('general', {}),
            jobs=profile_data.get('jobs', []),
            schools=profile_data.get('schools', []),
            skills=profile_data.get('skills', []),
            interests=profile_data.get('interests', {}),
            accomplishments=profile_data.get('accomplishments', {}),
            recommendations=profile_data.get('recommendations', {}),
            licenses=profile_data.get('licenses', []),
            query=profile_data.get('query', ''),
            created_at=datetime.now(tz.utc),
            updated_at=datetime.now(tz.utc)
        )
        
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def bulk_import_profiles(self, profiles_data: List[Dict[str, Any]]) -> Tuple[List[LinkedInProfile], List[Dict[str, Any]]]:
        """
        Import multiple LinkedIn profiles at once.
        
        Args:
            profiles_data: List of dictionaries containing LinkedIn profile data
        
        Returns:
            Tuple[List[LinkedInProfile], List[Dict[str, Any]]]: Tuple containing:
                - List of successfully imported profile objects
                - List of failed imports with error details
        """
        imported_profiles = []
        failed_imports = []
        
        for profile_data in profiles_data:
            try:
                profile = self.import_profile(profile_data)
                imported_profiles.append(profile)
            except Exception as e:
                error_detail = {
                    'profile_url': profile_data.get('general', {}).get('profileUrl'),
                    'error': str(e)
                }
                failed_imports.append(error_detail)
                continue
                
        return imported_profiles, failed_imports

    def get_profile_by_url(self, profile_url: str) -> LinkedInProfile:
        """
        Retrieve a profile by its LinkedIn URL.
        
        Args:
            profile_url: The LinkedIn profile URL
            
        Returns:
            LinkedInProfile: The profile object if found, None otherwise
        """
        return self.db.query(LinkedInProfile).filter_by(profile_url=profile_url).first()
