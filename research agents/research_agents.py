from dotenv import load_dotenv
from langchain.agents import create_agent 
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

from prompts import SYSTEM_PROMPT
from tools import fetch_text_from_url

load_dotenv()
model = init_chat_model(
    "gemini-1.5z-flash",
    model_provider="google-genai",
    temperature = 0.5,
    timeout = 600,
    max_tokens = 500,
)

checkpointer = InMemorySaver()

agent = create_agent(
    model = model,
    tools = [fetch_text_from_url],
    system_prompt = SYSTEM_PROMPT,
    checkpointer = checkpointer,
)

content = """Fetch this URL and just return the first 5 lines.
URL: https://www.gutenberg.org/files/64317/64317-0.txt"""

result = agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-lc"}},
)
print(result["messages"][-1].content_blocks)