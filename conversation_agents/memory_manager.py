from langchain_community.chat_message_histories import SQLChatMessageHistory
from config.setting import settings


def get_session_history(session_id):
    return SQLChatMessageHistory(session_id=session_id, connection_string=settings.DB_URL)