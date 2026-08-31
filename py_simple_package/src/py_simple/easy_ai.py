# ⚠️️ WORK IN PROGRESS NOT IN PUBLIC API ⚠️

"""
easy_ai wraps common LangChain functionality to make it easier to use.
"""


def get_model(provider, model_name, api_key=None, base_url=None, timeout=30):
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
        ValueError: If `provider` isn't one of the supported providers.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import get_model

            model = get_model("anthropic", "claude-sonnet-4-6")
            response = model.invoke("Hello!")
            ```

        === "The Traditional Way"
            ```python
            from langchain_anthropic import ChatAnthropic

            model = ChatAnthropic(
                model_name="claude-sonnet-4-6",
                timeout=30,
                stop=None
            )
            response = model.invoke("Hello!")
            ```
    """

    provider = provider.lower()

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model_name, api_key=api_key,
                          base_url=base_url)

    elif provider == "ollama":
        from langchain_ollama import ChatOllama
        url = base_url if base_url else "http://localhost:11434"
        return ChatOllama(model=model_name, base_url=url)

    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model_name=model_name,
            timeout=timeout,
            stop=None
        )

    elif provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model=model_name,
                                      google_api_key=api_key)

    elif provider == "mistral":
        from langchain_mistralai import ChatMistralAI
        return ChatMistralAI(api_key=api_key)

    else:
        raise ValueError(f"Provider '{provider}' is not supported yet!")
