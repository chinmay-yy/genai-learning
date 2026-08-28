from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI


load_dotenv()

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words for a beginner."
)

model = ChatMistralAI(model="mistral-small-latest")
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke("explain agents")

print(result)
