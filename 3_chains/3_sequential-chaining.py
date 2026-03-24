from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")
prompt_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ]
)

translation_template=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to telugu."),
        ("human", "Translate the following text: {text}"),
    ]
)

prepare_for_translation=RunnableLambda(lambda x: {"text" :x})

chain = prompt_template | llm | StrOutputParser() | translation_template | llm | StrOutputParser()

response = chain.invoke({"animal": "pig", "count": 2})

print(response)