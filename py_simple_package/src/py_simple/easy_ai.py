# ⚠️️ WORK IN PROGRESS NOT IN PUBLIC API ⚠️

"""
easy_ai wraps common LangChain functionality to make it easier to use.
"""


from langchain_core.language_models import BaseChatModel
from pydantic import SecretStr
from typing import Any


class EasyAIError(Exception):
    """
    Raised when a call to an AI model or provider cannot be completed.
    Args:
        message (str): Description of what went wrong.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def _is_exit_command(text: str) -> bool:
    """
    Checks whether a piece of user input should end the chat loop.

    Args:
        text (str): The raw text the user typed.

    Returns:
        True if `text` matches "exit", "quit", or "stop"
        (case-insensitive), False otherwise.
    """
    return text.lower() in ("exit", "quit", "stop")


def get_model(provider: str, model_name: str, api_key: str=None,
              base_url: str=None, timeout: int=30) -> BaseChatModel:
    """
    Returns a LangChain chat model instance for the given provider,
    without you having to remember each provider's import path and
    constructor arguments.

    Args:
        provider (str): Name of the LLM provider. One of "openai",
            "ollama", "anthropic", "google", or "mistral". Case-insensitive.
        model_name (str): Name of the model to use (e.g., "gpt-4o",
            "llama3", "claude-sonnet-4-6").
        api_key (str): API key for the provider, if required. Not used
            for "ollama". Defaults to None.
        base_url (str): Custom base URL for the provider. Used for
            "openai" and "ollama" (defaults to
            "http://localhost:11434" for ollama if not provided).
            Defaults to None.
        timeout (int): Request timeout in seconds. Currently only used
            for "anthropic". Defaults to 30.

    Returns:
        A LangChain chat model instance corresponding to the given
        provider.

    Raises:
        EasyAIError: If `provider` isn't one of the supported providers.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import get_model

            model = get_model("anthropic", "claude-sonnet-4-6")
            ```

        === "The Traditional Way"
            ```python
            from langchain_anthropic import ChatAnthropic

            model = ChatAnthropic(
                model_name="claude-sonnet-4-6",
                timeout=30,
                stop=None
            )
            ```
    """

    provider = provider.lower()

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(model=model_name, api_key=api_key,
                          base_url=base_url)
        return model

    elif provider == "ollama":
        from langchain_ollama import ChatOllama
        url = base_url if base_url else "http://localhost:11434"
        model = ChatOllama(model=model_name, base_url=url)
        return model

    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        api_key = SecretStr(api_key) if api_key is not None else None
        model = ChatAnthropic(
            model_name=model_name,
            api_key=api_key,
            timeout=timeout,
            stop=None
        )
        return model

    elif provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        model = ChatGoogleGenerativeAI(model=model_name,
                                      google_api_key=api_key)
        return model

    elif provider == "mistral":
        from langchain_mistralai import ChatMistralAI
        model = ChatMistralAI(api_key=api_key,
                              model_name=model_name)
        return model

    else:
        raise EasyAIError(f"\n\n\nERROR: Provider '{provider}' "
                          f"is not supported yet!")


def ask_ai(ai_model: BaseChatModel, question: str) -> (
        str | list[str | dict[Any, Any]]):
    """
    Sends a question to a LangChain chat model and returns the
    content of the response, without you having to reach into the
    returned message object yourself.

    Args:
        ai_model (BaseChatModel): A LangChain chat model instance,
            such as one returned by `get_model()`.
        question (str): The question or prompt to send to the model.

    Returns:
        The model's response content. Usually a plain string, but
        some providers may return a list of content blocks instead.

    Raises:
        EasyAIError: If the underlying call to the model fails for
            any reason (e.g. invalid API key, network error, timeout).

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import get_model, ask_ai

            model = get_model("anthropic", "claude-sonnet-4-6")
            answer = ask_ai(model, "hi")
            ```

        === "The Traditional Way"
            ```python
            from langchain_anthropic import ChatAnthropic

            model = ChatAnthropic(model_name="claude-sonnet-4-6")
            answer = model.invoke("hi").content
            ```
    """
    try:
        message = ai_model.invoke(question).content
        return message
    except Exception as e:
        raise EasyAIError(f"\n\n\nERROR: {e}") from None


def ai_chat(ai_model: BaseChatModel) -> None:
    """
    Runs an interactive chat loop in the terminal against a LangChain
    chat model, without you having to write the input/print loop or
    exit handling yourself.

    Prompts for input with "You: ", prints each reply prefixed with
    "AI: ", and keeps going until the user types "exit", "quit", or
    "stop". Errors from `ask_ai()` are caught and
    printed instead of raising, so a single bad call doesn't end the
    session.

    Args:
        ai_model (BaseChatModel): A LangChain chat model instance,
            such as one returned by `get_model()`.

    Returns:
        None. Runs until the user exits the loop.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import get_model, ai_chat

            model = get_model("anthropic", "claude-sonnet-4-6")
            ai_chat(model)
            ```

        === "The Traditional Way"
            ```python
            from langchain_anthropic import ChatAnthropic

            model = ChatAnthropic(model_name="claude-sonnet-4-6")

            while True:
                user_input = input("You: ")
                if user_input.lower() in ("exit", "quit", "stop"):
                    break
                print(f"AI: {model.invoke(user_input).content}")
            ```
    """

    while True:
        try:
            user_input = input("You: ")
            if _is_exit_command(user_input):
                break
            print(f"AI: {ask_ai(ai_model, user_input)}")
        except Exception as e:
            print(f"AI: {e}")
