# LinkedIn Profiles Directory

This directory is used to store downloaded LinkedIn profile data files.

## Directory Structure
```
linkedin_profiles/
├── *.json           # Profile data files
└── README.md        # This file
```

## File Format
Each profile is stored as a JSON file with the following naming convention: `username_YYYY_MM_DD.json`

The JSON structure includes:
```json
{
    "profile_url": "https://www.linkedin.com/in/username",
    "full_name": "Full Name",
    "headline": "Professional Headline",
    "summary": "Profile Summary",
    "experiences": [
        {
            "title": "Job Title",
            "company": "Company Name",
            "description": "Role Description",
            "start_date": "YYYY-MM",
            "end_date": "YYYY-MM"
        }
    ],
    "education": [
        {
            "school": "School Name",
            "degree": "Degree Name",
            "field": "Field of Study",
            "start_date": "YYYY",
            "end_date": "YYYY"
        }
    ],
    "skills": ["Skill 1", "Skill 2"],
    "interests": ["Interest 1", "Interest 2"],
    "accomplishments": ["Accomplishment 1", "Accomplishment 2"],
    "recommendations": ["Recommendation 1", "Recommendation 2"]
}
```

## Usage
1. Place your downloaded LinkedIn profile JSON files in this directory
2. The import script will process these files and add them to the database
3. After successful import, files can be archived or removed
