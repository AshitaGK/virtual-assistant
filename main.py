from fastapi import FastAPI, Request
import logging

# Configure logging to write to app.log with timestamps
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Define intents and their corresponding keywords for simple matching
intents = {
    "play_music": ["play music", "music please", "start music"],
    "turn_on_light": ["turn on light", "light on", "switch light on"]
}

def recognize_intent(text):
    """
    Recognize intent using simple keyword matching.
    Converts input to lowercase and strips whitespace for consistency.
    Returns the intent if matched, otherwise "unknown".
    """
    text = text.lower().strip()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if text == keyword:
                return intent
    return "unknown"

def get_response(intent):
    """
    Map recognized intent to a response message.
    Returns a user-friendly message based on the intent.
    """
    if intent == "play_music":
        return "Playing music now."
    elif intent == "turn_on_light":
        return "Turning on the light."
    else:
        return "I don't understand that."

# API endpoint to process user input
@app.post("/process")
async def process_request(request: Request):
    """
    Handle POST requests to /process, log the request and response,
    and return the assistant's response.
    """
    data = await request.json()
    text = data.get("text")
    logger.info(f"Received request: {request.method} {request.url.path} with text: {text}")
    intent = recognize_intent(text)
    response = get_response(intent)
    logger.info(f"Response: {response}")
    return {"response": response}

# Health check endpoint for monitoring
@app.get("/health")
async def health_check():
    """
    Return health status for monitoring purposes.
    """
    return {"status": "ok"}
