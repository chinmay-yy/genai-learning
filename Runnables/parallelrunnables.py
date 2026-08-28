from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import RunnableParallel, RunnableLambda

load_dotenv()

# MODEL COMPONENT
model = ChatMistralAI(model="mistral-small-latest")
parser = StrOutputParser()

# SHORT PROMPT
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 2-3 line simple words for a beginner."
)

# DETAILED PROMPT
detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail with examples for a beginner."
)

# INPUT
topic = "Machine Learning"

# # DICTIONARY OF CHAIN
# chain = RunnableParallel(
#     short=short_prompt | model | parser,
#     detailed=detailed_prompt | model | parser
# )

# result = chain.invoke({"topic": "Machine Learning"})
# print(result['short'])
# print(result['detailed'])

# DICTIONARY OF CHAIN for multi topics

chain = RunnableParallel({
    "short": RunnableLambda(lambda x: x['short']) | short_prompt | model | parser,
    "detailed": RunnableLambda(lambda x: x['detailed']) | detailed_prompt | model | parser
})

result = chain.invoke({
    "short" : {"topic": "AI agents"},
    "detailed": {"topic": "Agentic AI"}
})
print(result['short'])
print(result['detailed'])