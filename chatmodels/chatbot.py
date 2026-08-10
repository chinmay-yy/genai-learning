from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2603",
)

messeges = [
    system_message := SystemMessage(content="You are a funny helpful assistant."),
]            
# A SIMPLE WAY TO STORE THE CONVERSATION HISTORY, 
# NOT A STANDARD WAY TO STORE THE CONVERSATION HISTORY BUT A TEMPORARY TRICK

print("---------------------------------------------------------" )
print("-------------------WELLCOME TO CHATBOT-------------------" )
print("Type 'exit' or '0' to quit the chatbot.")
print("---------------------------------------------------------" )
while True: # INFINITE LOOP
    
    prompt = input("You : ")
    messeges.append(HumanMessage(content=prompt))
    if prompt == "exit" or prompt == "0":
        break
    response = llm.invoke(messeges, max_tokens=1000)
    messeges.append(AIMessage(content=response.content))

    print("Bot : " + response.content)

print(messeges)
