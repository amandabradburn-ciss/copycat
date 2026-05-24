# CopyCat

CopyCat is a web-based code analysis tool that analyzes Python code for common security vulnerabilities and provides AI-generated explanations and suggested fixes.

## Team Members
- Amanda Bradburn – Backend / Security / Integration
- Will Davis – AI / LLM Integration
- Nolan Biggers – Frontend

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Static Analysis: Bandit
- AI Integration: Google Gemini API
- CI/CD: GitHub Actions
- Testing: PyTest

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
- AI-generated vulnerability explanations and suggested fixes
- Vulnerability findings displayed in browser
- JSON communication between frontend and backend
- Enhanced AI mode support using optional passcodes
- Basic multi-language beta support (JavaScript, Java, C++)
- Logging and backend request monitoring
- GitHub Actions CI workflow for automated testing and scanning

# Current Status
The frontend and backend are fully integrated and operational. Users can submit Python code through the web interface, and the backend performs static analysis using Bandit before sending findings to the AI analysis system.

The project also includes a GitHub Actions CI pipeline that automatically installs dependencies, runs backend tests, and performs Bandit security scans on every push to the repository.

Additional beta language selections were added to demonstrate future expansion capabilities for multi-language support.

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

## Environment Variables

Create a `.env` file inside the backend folder:

```text
GEMINI_API_KEY=your_api_key_here
PASSCODE1=your_passcode_here
PASSCODE2=your_passcode_here
```

A sample `.env.example` file is included in the repository.

Optional passcodes allow access to enhanced AI model modes during hosted demonstrations.

# Setup Instructions

## Live Demo

Hosted version:

```text
https://web.williamodavis.me/copycat/frontend/
```

The live deployment connects the frontend interface to the hosted Flask backend and allows users to submit Python code for analysis directly through the browser.

## Local Development Setup

### Backend Setup

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

### Frontend Setup

Open:

```text
frontend/index.html
```

in a browser while the Flask backend is running locally.

## Example API Request

Example curl request to the Flask backend:

```bash
curl -X POST http://127.0.0.1:5000/submit \
-H "Content-Type: application/json" \
-d '{"text":"user_input = input()\neval(user_input)"}'
```

## Testing

Basic backend unit tests were implemented using PyTest and integrated into the GitHub Actions CI pipeline.

Run tests locally with:

```bash
PYTHONPATH=. pytest
```

The CI workflow automatically:
- Installs backend dependencies
- Runs backend unit tests
- Performs Bandit security scans
- Validates backend stability on push

## Security and Static Analysis

Bandit was used for static analysis of submitted Python code and backend security testing.

Example vulnerabilities identified include:
- Unsafe use of eval()
- Insecure subprocess usage
- Debug mode enabled in Flask

Security findings are displayed to the user along with AI-generated explanations, severity levels, CWE references, and suggested mitigation guidance.

Known limitations and future hardening tasks are documented through the project issue tracking system.