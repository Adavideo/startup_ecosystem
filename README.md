# Startup Ecosystem Enabler

A Python application that manages a startup community ecosystem by importing LinkedIn profiles of founders and mentors, and providing intelligent matching capabilities using RAG (Retrieve Augmented Generation).

## Features

- LinkedIn profile import and management
- Intelligent mentor-startup matching (upcoming)
- RAG-based search and recommendations (upcoming)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following variables:
```
DATABASE_URL=sqlite:///startup_ecosystem.db
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## Project Structure

```
startup_ecosystem/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── profile.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── profile.py
│   └── services/
│       ├── __init__.py
│       ├── linkedin_import.py
│       └── rag_service.py
├── requirements.txt
└── README.md
```
