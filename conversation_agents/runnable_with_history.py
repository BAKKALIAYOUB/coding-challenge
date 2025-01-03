from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from .memory_manager import get_session_history


def create_runnable_with_history(runnable):
    """
    Creates a `RunnableWithMessageHistory` instance that integrates with a given runnable.

    Args:
        runnable: The underlying runnable (e.g., an Ollama model).
        input_key (str): The key for the input message in the input dictionary.

    Returns:
        RunnableWithMessageHistory: A runnable that supports message history.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant that respond to users task/question based on you knowledge and history"),
        MessagesPlaceholder(variable_name="history"),
        MessagesPlaceholder(variable_name="input"),
    ])
    chain = prompt | runnable
    return RunnableWithMessageHistory(
        runnable=chain,  # The underlying runnable (Models)
        get_session_history=get_session_history,  # Function to retrieve session history
        input_messages_key="input",
        history_messages_key="history",
    )
