import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is loaded
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Create external Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set up the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configure the run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Smart Translator Agent
agent = Agent(
    name="Translator",
    instructions=(
        "You are a smart translator. Detect whether the input language is English or Urdu. "
        "Then translate it to the opposite language.\n"
        "- If the input is in English, reply only in simple Urdu.\n"
        "- If the input is in Urdu, reply only in simple English.\n"
        "Always return only the translated sentence without any explanation."
    ),
    model=model
)

# input_text = "میرا نام مسکان ہے، میں جی آئی اے آئی سی کی طالبہ ہوں۔"
input_text = "My name is Muskan and I study at GIAIC."

# Run agent with input
response = Runner.run_sync(
    agent,
    input=input_text,
    run_config=config
)

# Show the result
print(response.final_output)






