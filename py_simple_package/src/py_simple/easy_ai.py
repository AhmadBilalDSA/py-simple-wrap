# ⚠️️ WORK IN PROGRESS NOT IN PUBLIC API ⚠️


def get_model(provider, model_name, api_key=None, base_url=None, timeout=30):
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
