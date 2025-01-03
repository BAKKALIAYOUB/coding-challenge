from langchain_ollama.llms import OllamaLLM


class MyOllamaModel(OllamaLLM):
    """
    A custom class that extends the `OllamaLLM` class to initialize an Ollama language model
    with a specified model name.

    This class is designed to simplify the initialization of an Ollama model by allowing
    the user to pass the model name directly during instantiation.
    """

    def __init__(self, model_name: str):
        """
        Initializes the `MyOllamaModel` instance with the specified Ollama model name.

        Args:
            model_name (str): The name of the Ollama model to be used. This should correspond
                            to a valid Ollama model available in your environment.

        Example:
            >>> my_model = MyOllamaModel(model_name="example-model")
            >>> # Now `my_model` is ready to use for text generation or other tasks.
        """
        super().__init__(model=model_name)