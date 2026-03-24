from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define the summary template
summary_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You are a movie critic."),
        ("human", "Summarize the movie {movie} in detail.")
    ]
)

# Define functions for plot analysis and character analysis

def plot_analysis(text):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the plot of the movie {text} in detail.")
        ]
    )
    return prompt.format_prompt(text=text)

def character_analysis(character):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the character of {character} in detail.")
        ]
    )
    return prompt.format_prompt(character=character)



    # Function to combine plot analysis and character analysis results

def combine_analysis(plot_analysis, character_analysis):
    return f"Plot Analysis:\n {plot_analysis}\n\nCharacter Analysis:\n {character_analysis}"



#parallel branches for plot analysis and character analysis
plot_branch_chain = RunnableLambda(lambda x: plot_analysis(x)) | llm | StrOutputParser()
character_branch_chain = RunnableLambda(lambda x: character_analysis(x)) | llm | StrOutputParser()



#final chain combining summary, parallel plot and character analysis, and then combining the results
chain =summary_template | llm | StrOutputParser() | RunnableParallel({
    "plot_analysis": plot_branch_chain,
    "character_analysis": character_branch_chain
}) | RunnableLambda(lambda x: combine_analysis(x["plot_analysis"], x["character_analysis"]))   
 
 # Invoke the chain with the movie name
response = chain.invoke({"movie": "Athadu"})

print(response)