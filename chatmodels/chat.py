# using init_chat_model()

# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model

# load_dotenv()

# model = init_chat_model(
#     "llama-3.1-8b-instant",
#     model_provider="groq",
# )

# response = model.invoke("What is the capital of France?")

# print(response.content)


# using library modules

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
# )

# response = llm.invoke("What is the capital of France?")

# print(response.content)

#  using mistral ai 

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2603",
)

response = llm.invoke("write a paragraph about the interesting thing about the capital of France?", max_tokens=100)

print(response.content)