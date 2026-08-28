from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# MODEL COMPONENT
model = ChatMistralAI(model="mistral-small-latest")
parser = StrOutputParser()

# CODE PROMPT
code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that generates code."),
    ("user", "Generate code for the following problem:\n{problem}")
])  

# EXPLANATION PROMPT
explanation_prompt = ChatPromptTemplate.from_messages([
    ("system"," You are a helpful assistant that explains code."),
    ("user", "Explain the following code:\n{code}")
])

seq = code_prompt | model | parser

seq2 = RunnableParallel({
    "code" : RunnablePassthrough(),
    "explanation" : (
        RunnableLambda(lambda code: {"code": code})
        | explanation_prompt
        | model
        | parser
    )
})

chain = seq | seq2

result = chain.invoke({"problem" : "write a code of palindrome"})

print(result['code'])
print(result['explanation'])