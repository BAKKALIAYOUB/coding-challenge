from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.ollama import MyOllamaModel
from config.setting import settings
from conversation_agents.ollama_agent import ConversationAgent

# Initialize FastAPI app
app = FastAPI()

# Initialize the Ollama model
ollamamodel = MyOllamaModel(model_name=settings.OLLAMA_MODEL)

# Dictionary to store conversation agents for each session
agents = {}

# Pydantic models for request bodies
class StartConversationRequest(BaseModel):
    sessionid: str

class ChatRequest(BaseModel):
    sessionid: str
    message: str

@app.post("/start_conversation")
def start_conversation(request: StartConversationRequest):
    """
    Starts a new conversation with a unique session ID.
    """
    sessionid = request.sessionid
    if not sessionid:
        raise HTTPException(status_code=400, detail="sessionid is required")

    # Check if a conversation already exists for this sessionid
    if sessionid in agents:
        raise HTTPException(status_code=400, detail="Conversation already started for this sessionid.")

    # Initialize the conversation agent
    agents[sessionid] = ConversationAgent(sessionid=sessionid, model=ollamamodel)
    return {"message": f"Conversation started with sessionid: {sessionid}"}

@app.post("/chat")
def chat(request: ChatRequest):
    """
    Sends a message to the conversation agent and returns the response.
    """
    sessionid = request.sessionid
    message = request.message

    if not sessionid:
        raise HTTPException(status_code=400, detail="sessionid is required")
    if not message:
        raise HTTPException(status_code=400, detail="message is required")

    # Retrieve the conversation agent for the sessionid
    agent = agents.get(sessionid)
    if not agent:
        raise HTTPException(status_code=400, detail="Conversation not started. Call /start_conversation first.")

    # Generate a response from the agent
    response = agent.generate_response(message)
    return {"response": response}

@app.post("/end_conversation")
def end_conversation(request: StartConversationRequest):
    """
    Ends the conversation for the given session ID.
    """
    sessionid = request.sessionid
    if not sessionid:
        raise HTTPException(status_code=400, detail="sessionid is required")

    # Remove the conversation agent for the sessionid
    if sessionid in agents:
        del agents[sessionid]
        return {"message": f"Conversation ended for sessionid: {sessionid}"}
    else:
        raise HTTPException(status_code=404, detail="No active conversation found for this sessionid.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)