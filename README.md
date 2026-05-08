# CopyCat

CopyCat is a web-based code analysis tool that analyzes Python code for common security vulnerabilities and provides AI-generated explanations and suggested fixes.

## Team Members
- Amanda Bradburn – Backend / Security / Integration
- Will Davis – AI / LLM Integration
- Nolan Biggers – Frontend

## Tech Stack
- Frontend: HTML, CSS, minimal JavaScript
- Backend: Python, Flask
- Static Analysis: Bandit
- AI: Gemma

## MVP
- User submits Python code
- Backend analyzes code with Bandit
- AI explains detected vulnerabilities
- Website displays findings and suggested fixes

---

# Current Features
- Frontend interface for code submission
- Flask backend API
- Python code scanning using Bandit
- Vulnerability findings displayed in browser
- JSON communication between frontend and backend

# Current Status
The backend and frontend are successfully connected. Users can submit Python code through the web interface, and the backend performs static analysis using Bandit.

# Example Vulnerability Detection

Example input:

```python
user_input = input()
eval(user_input)
```

Bandit detects the insecure use of `eval()` and reports the associated vulnerability information, including severity and confidence level.

## Repository Structure

```text
frontend/   - HTML/CSS/JavaScript frontend
backend/    - Flask backend and Bandit integration
```

# Setup Instructions

## Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

## Frontend Setup

Open:

```text
frontend/index.html
```

in a browser while the Flask backend is running.
