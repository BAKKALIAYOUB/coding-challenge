from models.ollama import MyOllamaModel
from config.setting import settings
from conversation_agents.ollama_agent import ConversationAgent

mymodel = MyOllamaModel(model_name=settings.OLLAMA_MODEL)
agent = ConversationAgent(sessionid="skhdskjdsdnsd", model=mymodel)

response = agent.generate_response("d'accord merci beacoup")
print(response)