from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")


template=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful legal assistant that provides concise answers to questions based in {country}."),
    ("human", " if i  jump {count} red signal what cases would file on me ?")
])

# Create the combined chain using LangChain Expression Language (LCEL)
chain=template | llm | StrOutputParser()

# Invoke the chain
result = chain.invoke({"country": "India","count":5})

print(result)