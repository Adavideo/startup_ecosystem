# LinkedIn Profiles Directory

This directory is used to store downloaded LinkedIn profile data files.

## Directory Structure
```
linkedin_profiles/
├── founders/        # Founder profiles
├── mentors/         # Mentor profiles
└── README.md        # This file
```

## File Format
Each profile should be stored as a JSON file with the following structure:
```json
{
    "id": "linkedin-profile-id",
    "fullName": "Full Name",
    "headline": "Professional Headline",
    "summary": "Profile Summary",
    "currentCompany": "Current Company Name",
    "industry": "Industry",
    "location": "Location",
    "experience": [
        {
            "title": "Job Title",
            "company": "Company Name",
            "description": "Job Description",
            "startDate": "Start Date",
            "endDate": "End Date"
        }
    ],
    "skills": ["Skill 1", "Skill 2", "Skill 3"],
    "education": [
        {
            "school": "School Name",
            "degree": "Degree Name",
            "field": "Field of Study",
            "startDate": "Start Date",
            "endDate": "End Date"
        }
    ]
}
```

## Usage
1. Place your downloaded LinkedIn profile JSON files in this directory
2. The import script will process these files and add them to the database
3. After successful import, files can be archived or removed
