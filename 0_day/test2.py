from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

messages =[SystemMessage(content=" You are a sarcastic assistant who answers in exactly one sentence"),
HumanMessage(content = "what is virtual environment in python")]

load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant")
response= llm.invoke(messages)
print(response.content)
