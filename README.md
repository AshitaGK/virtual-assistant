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
   
2.  **Set up virtual environment**:
     ```bash
     python -m venv venv
     source venv/bin/activate

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

   ```
4. **Run the Application**:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000

    ```
 5. **Test the application:**      
   - Health check of API:-
    ```bash
    curl http://localhost:8000/health
    ```
   

   - Processing input:-
     ```bash
     curl -X POST "http://localhost:8000/process" -H "Content-Type: application/json" -d '{"text": "play music"}'
     ```
     Expected output: {"response": "Playing music now.."}
     
    

    
