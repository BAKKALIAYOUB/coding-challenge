from models.ollama import MyOllamaModel
from config.setting import settings
from conversation_agents.ollama_agent import ConversationAgent

mymodel = MyOllamaModel(model_name=settings.OLLAMA_MODEL)
agent = ConversationAgent(sessionid="your session id", model=mymodel)

response = agent.generate_response("Your question")
print(response)