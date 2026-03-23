## a local chatgpt made in terminal 
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant")

chat_history = [] #uses a list to store the conversation history

system_message = SystemMessage(content=" You are a helpful assistant who answers in a friendly manner") # sets the system message to define the assistant's behavior
chat_history.append(system_message) # adds the system message to the chat history

while True:
    query=input("you: ") #takes users input
    if query.lower()== "exit":
        break # exits loop if user types exit
    chat_history.append(HumanMessage(content=query)) # adds user message to chat history
    response=llm.invoke(chat_history) # gets response from the model based on chat history
    print("AI :",response.content) # prints the AI response
    chat_history.append(AIMessage(content=response.content)) # adds AI response to chat history for future context
    
print("Conversation ended.")

print("Conversation history:")
for message in chat_history:    print(f"{message.__class__.__name__}: {message.content}") # prints the entire conversation history with message type and content