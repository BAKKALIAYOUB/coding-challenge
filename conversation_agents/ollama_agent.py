from .runnable_with_history import create_runnable_with_history
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import SQLChatMessageHistory
from config.setting import settings

class ConversationAgent:
    def __init__(self, sessionid: str, model):
        self.sessionid = sessionid
        self.model = model
        self.history = SQLChatMessageHistory(
            session_id=sessionid,
            connection_string=settings.DB_URL
        )
        self.model_with_hisory = create_runnable_with_history(
            runnable=self.model
        )
        
    def generate_response(self, message):
        response = self.model_with_hisory.invoke(
            {"input": [HumanMessage(content=message)]},
            config={"configurable": {"session_id": self.sessionid}},

        )

        return response
        
    def get_history(self):
        return self.history.get_messages()