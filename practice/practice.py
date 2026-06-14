from langchain.agent import create_agent
from langchain.chat_models import init_chat_model

'''agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools = [expensive_car],
    system_prompt="you are a car recommendation assistant always use the expensive_car tool to recommend cars for people."
) '''

''' //static way
agnet = create_agent(
    "google_genai:gemini-2.5-flash-lite",
    tool = tools
) '''

''' //with full cantrol using init_chat_model


'''
