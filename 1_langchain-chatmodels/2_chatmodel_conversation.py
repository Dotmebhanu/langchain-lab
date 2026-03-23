from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant")
messages =[SystemMessage(content=" You are a sarcastic assistant who answers in exactly one sentence"),
HumanMessage(content = "what is virtual environment in python"),
AIMessage(content = "A virtual environment in Python is like a bubble where you can install packages without affecting the rest of your system, because who wants to mess with their global Python setup, right?"),
 HumanMessage(content="Can you explain it in more detail?")]

response= llm.invoke(messages)


print(response.content)