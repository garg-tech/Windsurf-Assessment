# Resume Skill Extractor

A Streamlit-based application that extracts skills and information from resumes using AI/LLM capabilities.

## Features

- Upload PDF resumes
- Extract key information (Name, Email, Phone)
- Extract and categorize skills
- Extract experience
- Store and retrieve processed resumes
- User-friendly interface built with Streamlit

## Prerequisites

- Docker installed on your system
- Google API Key for LLM capabilities

## Setup

1. Clone the repository
2. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
3. Edit the `.env` file with your credentials:
   ```bash
   GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
   ```

## Running with Docker

### Build and Run

1. Build the Docker image:
   ```bash
   docker build -t resume-skill-extractor .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 --env-file .env resume-skill-extractor
   ```

   The application will be available at http://0.0.0.0:8501

## Project Structure

- `app.py`: Main Streamlit application file
- `parser.py`: Contains resume parsing logic
- `storage.py`: Handles data storage operations
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `.env.example`: Environment variables template

## Environment Variables

- `GOOGLE_API_KEY`: Required for LLM capabilities

## Usage

1. Open the application in your web browser at http://0.0.0.0:8501
2. Click "Browse files" to upload a PDF resume
3. The application will automatically extract and display:
   - Name
   - Email
   - Phone
   - Skills
   - Experience
   

## Note

- Ensure you have a valid Google API Key with the necessary permissions
- The application stores processed resumes in `stored_resumes.jsonl`
- Make sure to keep your `.env` file secure and never commit it to version control
