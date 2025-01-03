# LangChain LLM Conversation Agent

This project provides a conversational AI agent powered by LhangChain and Exposes it as REST API using FastAPI.
The Agent leverages a language model (LLM) to handle user queries and maintains conversation hisotry for context-aware responses.

## Features
* **Conversational AI Agent**: Built using LangChain, the agent can handle user queries with context from conversation history.
* **FastAPI Endpoint**: Exposes the agent as a REST API for easy integration with other applications.
* **Session Management**: Supports multiple conversation sessions with unique session IDs.
* **Customizable Prompt**: The agent's behavior can be customized by modifying the system prompt.
## Prerequisites
Before running the project, ensure you have the follwing intalled:
* Python 3.10 or higher
* `pip`
* Docker (optional, for containerized deployment)

## Installation
1. clone the repository:
2. Install dependencies:\
    ```bash
      pip install -r requirement.txt
    ```
3. Set Up Environment Variables:\
    Add required environment variable such as OpenAI API key (if you openai LLMs), or ollam mode name\
    ```bash
    cp .env.example .env
    ```
4. Pull ollama model: \
    ```bash
   ollama pull llama3.1:1b
    ```

## Usage
### Running the FastAPI Server
To start the FastAPI server, run the following command:\
```bash
uvicorn main:app
```
The server will start at `http://127.0.0.1:8000`

## Docker Deployment
To Deploy the application using Docker:
1. **Build the Docker Image**:
    ```bash
   docker build -t image-name .
    ```
2. **Run The Docker container**:
    ```bash
   docker run -p 8000:8000 image-name
    ```
The API will be accessible at `http://127.0.0.1:8000`

## Project Structure
```
.
├── .env                         # Environment variables
├── .env.example                 # Example environment variables file
├── .gitignore                   # Specifies files to ignore in Git
├── app.py                       # FastAPI application and endpoints
├── Dockerfile                   # Docker configuration
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── memory.db                    # SQLite database for storing conversation history
├── usage_example.py             # Example usage of the conversation agent
├── conversation_agents/         # Contains conversation agent-related modules
│   ├── __init__.py
│   ├── memory_manager.py        # Manages session history and memory
│   ├── ollama_agent.py          # Implementation of the Ollama-based agent
│   ├── runnable_with_history.py # Runnable with message history integration
    └── agent.py                 # Contain Ollama Agent for chat  
├── models/                      # Contains model-related modules
│   ├── __init__.py
│   └── ollama.py                # Ollama model implementation
└── config
    ├──__init__.py               
    └── setting.py               #conatin envirnment variables
```