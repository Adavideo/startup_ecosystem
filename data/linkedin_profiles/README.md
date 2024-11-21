# LinkedIn Profiles Directory

This directory is used to store downloaded LinkedIn profile data files.

## Directory Structure
```
linkedin_profiles/
├── *.json           # Profile data files
└── README.md        # This file
```

## File Format
Each file contains a list of LinkedIn profiles and follows the naming convention: `username_YYYY_MM_DD.json`

The JSON structure includes:
```json
[
    {
        "general": {
            "imgUrl": "URL to profile image",
            "profileUrl": "https://www.linkedin.com/in/username",
            "connectionDegree": "1st/2nd/3rd",
            "firstName": "First Name",
            "lastName": "Last Name",
            "fullName": "Full Name",
            "location": "City, State, Country",
            "headline": "Professional Headline",
            "backgroundUrl": "URL to background image",
            "userId": "LinkedIn User ID",
            "vmid": "LinkedIn VMID"
        },
        "jobs": [
            {
                "companyUrl": "URL to company profile",
                "companyName": "Company Name",
                "logoUrl": "URL to company logo",
                "jobTitle": "Job Title",
                "dateRange": "Employment Date Range",
                "description": "Job Description",
                "location": "Job Location"
            }
        ],
        "schools": [
            {
                "schoolUrl": "URL to school profile",
                "schoolName": "School Name",
                "logoUrl": "URL to school logo",
                "degree": "Degree Name",
                "field": "Field of Study",
                "dateRange": "Education Date Range"
            }
        ],
        "skills": [
            {
                "name": "Skill Name",
                "endorsements": 0
            }
        ],
        "interests": {
            "influencers": [
                {
                    "url": "URL to influencer profile",
                    "name": "Influencer Name"
                }
            ],
            "companies": [
                {
                    "url": "URL to company profile",
                    "name": "Company Name",
                    "count": "Follower Count"
                }
            ],
            "groups": [
                {
                    "url": "URL to group",
                    "name": "Group Name",
                    "count": "Member Count"
                }
            ],
            "schools": [
                {
                    "url": "URL to school profile",
                    "name": "School Name",
                    "count": "Follower Count"
                }
            ]
        },
        "accomplishments": {
            "courses": ["Course 1", "Course 2"],
            "languages": ["Language 1", "Language 2"]
        },
        "recommendations": {
            "receivedRecommendations": [
                {
                    "profileUrl": "URL to recommender profile",
                    "text": "Recommendation text"
                }
            ],
            "givenRecommendations": [
                {
                    "profileUrl": "URL to recipient profile",
                    "text": "Recommendation text"
                }
            ]
        },
        "licences": [
            {
                "name": "License Name",
                "credentialUrl": "URL to credential"
            }
        ]
    }
]
```

## Usage
1. Place your downloaded LinkedIn profile JSON files in this directory
2. The import script will process these files and add them to the database
3. After successful import, files can be archived or removed
