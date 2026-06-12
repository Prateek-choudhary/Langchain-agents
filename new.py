from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()
def expensive_car(person: str) -> str:
    """Get expensive car for a given person."""
    return f" {person} should get a ferrari"

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[expensive_car],
    system_prompt="You are a car recommendation assistant. Always use the expensive_car tool to recommend cars for people.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "what car sarthak should get?"}]}
)
print(result["messages"][-2].content)

