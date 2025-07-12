# agents.py

class AsyncOpenAI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url


class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.openai_client = openai_client


class RunConfig:
    def __init__(self, model, model_provider, tracing_disabled=True):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled


class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model


class Runner:
    @staticmethod
    def run_sync(agent, input, run_config):
        # Simulated translation — yahan Gemini API call honi chahiye thi
        if "میرا نام" in input:
            return type("Response", (), {"final_output": "My name is Muskan, I am a student at GIAIC."})
        elif "My name" in input:
            return type("Response", (), {"final_output": "میرا نام مسکان ہے، میں جی آئی اے آئی سی کی طالبہ ہوں۔"})
        else:
            return type("Response", (), {"final_output": "Translation not available."})


