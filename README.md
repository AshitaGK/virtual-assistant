# AI Virtual Assistant

This is a simple AI virtual assistant built with FastAPI, designed to recognize user intents through basic keyword matching and respond accordingly. It includes logging for tracking requests and responses.

## Features
- **Intent Recognition**: Matches predefined keywords to intents (e.g., "play music" → "play_music").
- **API Endpoints**: 
  - `POST /process`: Processes user input and returns a response.
  - `GET /health`: Checks the API’s health status.
- **Logging**: Logs requests and responses to `logs/app.log` with timestamps.

## Prerequisites
- Python 3.9
- Docker (optional, for containerization)

## Project Structure
```
virtual-assistant/
├── main.py
├── requirements.txt
├── logs/
│   └── app.log (generated at runtime)
├── .gitignore
├── Dockerfile
└── README.md

```
## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd virtual-assistant

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

   ```
3. **Run the Application**:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000

    ```
       
